"""Generated from Smithy shape ``com.amazonaws.appstream#Platforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.platform_type

Platforms: TypeAlias = list["aws_sdk_appstream.types.platform_type.PlatformType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Platforms) -> list:
    import aws_sdk_appstream.types.platform_type

    out: list = []
    for item in value:
        out.append(aws_sdk_appstream.types.platform_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Platforms:
    import aws_sdk_appstream.types.platform_type

    out: Platforms = []
    for item in data:
        out.append(aws_sdk_appstream.types.platform_type.deserialize_aws_json_1_1(item))
    return out
