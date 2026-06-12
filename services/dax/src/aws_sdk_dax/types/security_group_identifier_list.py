"""Generated from Smithy shape ``com.amazonaws.dax#SecurityGroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dax.types.string

SecurityGroupIdentifierList: TypeAlias = list["aws_sdk_dax.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIdentifierList:
    return list(data)
