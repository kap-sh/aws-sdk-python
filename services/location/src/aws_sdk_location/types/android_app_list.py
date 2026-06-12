"""Generated from Smithy shape ``com.amazonaws.location#AndroidAppList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.android_app

AndroidAppList: TypeAlias = list["aws_sdk_location.types.android_app.AndroidApp"]


# --- restJson1 ser/de ---
def serialize_json(value: AndroidAppList) -> list:
    import aws_sdk_location.types.android_app
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.android_app.serialize_json(item))
    return out


def deserialize_json(data: list) -> AndroidAppList:
    import aws_sdk_location.types.android_app
    out: AndroidAppList = []
    for item in data:
        out.append(aws_sdk_location.types.android_app.deserialize_json(item))
    return out