"""Generated from Smithy shape ``com.amazonaws.securityir#ImpactedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_account_id

ImpactedAccounts: TypeAlias = list[
    "aws_sdk_security_ir.types.aws_account_id.AWSAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedAccounts) -> list:
    return list(value)


def deserialize_json(data: list) -> ImpactedAccounts:
    return list(data)
