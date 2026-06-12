"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Strings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.string

Strings: TypeAlias = list["aws_sdk_cloudhsm_v2.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Strings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Strings:
    return list(data)
