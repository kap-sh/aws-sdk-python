"""Generated from Smithy shape ``com.amazonaws.odb#Months``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.month

Months: TypeAlias = list["aws_sdk_odb.types.month.Month"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Months) -> list:
    import aws_sdk_odb.types.month

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.month.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Months:
    import aws_sdk_odb.types.month

    out: Months = []
    for item in data:
        out.append(aws_sdk_odb.types.month.deserialize_aws_json_1_0(item))
    return out
