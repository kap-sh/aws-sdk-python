"""Generated from Smithy shape ``com.amazonaws.location#AppleAppList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.apple_app

AppleAppList: TypeAlias = list["aws_sdk_location.types.apple_app.AppleApp"]


# --- restJson1 ser/de ---
def serialize_json(value: AppleAppList) -> list:
    import aws_sdk_location.types.apple_app
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.apple_app.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppleAppList:
    import aws_sdk_location.types.apple_app
    out: AppleAppList = []
    for item in data:
        out.append(aws_sdk_location.types.apple_app.deserialize_json(item))
    return out