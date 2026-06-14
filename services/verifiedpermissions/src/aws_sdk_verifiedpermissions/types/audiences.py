"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#Audiences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.audience

Audiences: TypeAlias = list["aws_sdk_verifiedpermissions.types.audience.Audience"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Audiences) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Audiences:
    return list(data)
