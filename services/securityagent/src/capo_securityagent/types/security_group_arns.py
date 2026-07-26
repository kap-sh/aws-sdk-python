"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityGroupArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.security_group_arn

SecurityGroupArns: TypeAlias = list[
    "capo_securityagent.types.security_group_arn.SecurityGroupArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupArns) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupArns:
    return list(data)
