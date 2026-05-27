"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAttributeName``."""

from typing import Literal, TypeAlias

ImageAttributeName: TypeAlias = Literal[
    "description",
    "kernel",
    "ramdisk",
    "launchPermission",
    "productCodes",
    "blockDeviceMapping",
    "sriovNetSupport",
    "bootMode",
    "tpmSupport",
    "uefiData",
    "lastLaunchedTime",
    "imdsSupport",
    "deregistrationProtection",
]
