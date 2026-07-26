"""Generated from Smithy shape ``com.amazonaws.odb#Months``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.month

Months: TypeAlias = list["capo_odb.types.month.Month"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Months) -> list:
    import capo_odb.types.month

    out: list = []
    for item in value:
        out.append(capo_odb.types.month.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Months:
    import capo_odb.types.month

    out: Months = []
    for item in data:
        out.append(capo_odb.types.month.deserialize_aws_json_1_0(item))
    return out
