"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAttributeName``."""

from typing import Literal, TypeAlias

InstanceAttributeName: TypeAlias = Literal[
    "instanceType",
    "kernel",
    "ramdisk",
    "userData",
    "disableApiTermination",
    "instanceInitiatedShutdownBehavior",
    "rootDeviceName",
    "blockDeviceMapping",
    "productCodes",
    "sourceDestCheck",
    "groupSet",
    "ebsOptimized",
    "sriovNetSupport",
    "enaSupport",
    "enclaveOptions",
    "disableApiStop",
]
