"""Generated from Smithy shape ``com.amazonaws.securityir#AWSAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_account_id

AWSAccountIds: TypeAlias = list["aws_sdk_security_ir.types.aws_account_id.AWSAccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AWSAccountIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AWSAccountIds:
    return list(data)