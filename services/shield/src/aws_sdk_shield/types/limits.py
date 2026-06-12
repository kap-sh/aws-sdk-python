"""Generated from Smithy shape ``com.amazonaws.shield#Limits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.limit

Limits: TypeAlias = list["aws_sdk_shield.types.limit.Limit"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Limits) -> list:
    import aws_sdk_shield.types.limit

    out: list = []
    for item in value:
        out.append(aws_sdk_shield.types.limit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Limits:
    import aws_sdk_shield.types.limit

    out: Limits = []
    for item in data:
        out.append(aws_sdk_shield.types.limit.deserialize_aws_json_1_1(item))
    return out
