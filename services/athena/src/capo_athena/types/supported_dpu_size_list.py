"""Generated from Smithy shape ``com.amazonaws.athena#SupportedDPUSizeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.integer

SupportedDPUSizeList: TypeAlias = list["capo_athena.types.integer.Integer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedDPUSizeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SupportedDPUSizeList:
    return list(data)
