"""Generated from Smithy shape ``com.amazonaws.lightsail#BundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bundle

BundleList: TypeAlias = list["aws_sdk_lightsail.types.bundle.Bundle"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleList) -> list:
    import aws_sdk_lightsail.types.bundle

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.bundle.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BundleList:
    import aws_sdk_lightsail.types.bundle

    out: BundleList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.bundle.deserialize_aws_json_1_1(item))
    return out
