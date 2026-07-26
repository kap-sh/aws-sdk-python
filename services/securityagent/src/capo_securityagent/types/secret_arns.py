"""Generated from Smithy shape ``com.amazonaws.securityagent#SecretArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.secret_arn

SecretArns: TypeAlias = list["capo_securityagent.types.secret_arn.SecretArn"]


# --- restJson1 ser/de ---
def serialize_json(value: SecretArns) -> list:
    return list(value)


def deserialize_json(data: list) -> SecretArns:
    return list(data)
