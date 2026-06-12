"""Generated from Smithy shape ``com.amazonaws.glue#PublicKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string

PublicKeysList: TypeAlias = list["aws_sdk_glue.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKeysList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PublicKeysList:
    return list(data)
