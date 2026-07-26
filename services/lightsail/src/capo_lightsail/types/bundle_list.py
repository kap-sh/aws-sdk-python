"""Generated from Smithy shape ``com.amazonaws.lightsail#BundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.bundle

BundleList: TypeAlias = list["capo_lightsail.types.bundle.Bundle"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleList) -> list:
    import capo_lightsail.types.bundle

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.bundle.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BundleList:
    import capo_lightsail.types.bundle

    out: BundleList = []
    for item in data:
        out.append(capo_lightsail.types.bundle.deserialize_aws_json_1_1(item))
    return out
