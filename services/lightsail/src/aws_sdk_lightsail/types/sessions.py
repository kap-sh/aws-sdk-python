"""Generated from Smithy shape ``com.amazonaws.lightsail#Sessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.session

Sessions: TypeAlias = list["aws_sdk_lightsail.types.session.Session"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sessions) -> list:
    import aws_sdk_lightsail.types.session

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.session.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Sessions:
    import aws_sdk_lightsail.types.session

    out: Sessions = []
    for item in data:
        out.append(aws_sdk_lightsail.types.session.deserialize_aws_json_1_1(item))
    return out
