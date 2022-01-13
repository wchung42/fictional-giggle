from tuya_iot import TuyaOpenAPI, TuyaDeviceManager, TuyaAssetManager, AuthType, TUYA_LOGGER
from tuya_iot.device import TuyaDevice

from config import ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD, ASSET_ID, DEVICE_ID
import requests
import random
import os
import logging

ENDPOINT = 'https://openapi.tuya{}.com'
COUNTRY_CODE = 'us'

TUYA_LOGGER.setLevel(logging.DEBUG)

# Initialize Tuya OpenAPI
openapi = TuyaOpenAPI(ENDPOINT.format(COUNTRY_CODE), ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
openapi.connect(USERNAME, PASSWORD, COUNTRY_CODE, 'tuyaSmart')


# Get asset list of the user
openapi.get('/v1.0/iot-03/users/assets', {
  'parent_asset_id': '',
  'page_no': 0,
  'page_size': 100,
})

# assetManager = TuyaAssetManager(openapi)
# devIds = assetManager.get_device_list(ASSET_ID)

# device_manager = TuyaDeviceManager(openapi)
