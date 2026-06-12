"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on

AddOnList: TypeAlias = list["aws_sdk_lightsail.types.add_on.AddOn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOnList) -> list:
    import aws_sdk_lightsail.types.add_on

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.add_on.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddOnList:
    import aws_sdk_lightsail.types.add_on

    out: AddOnList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.add_on.deserialize_aws_json_1_1(item))
    return out
