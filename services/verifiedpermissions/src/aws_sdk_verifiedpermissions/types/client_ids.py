"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ClientIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.client_id

ClientIds: TypeAlias = list["aws_sdk_verifiedpermissions.types.client_id.ClientId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClientIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ClientIds:
    return list(data)
