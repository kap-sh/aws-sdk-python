"""Generated from Smithy shape ``com.amazonaws.securityagent#SubnetArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.subnet_arn

SubnetArns: TypeAlias = list["capo_securityagent.types.subnet_arn.SubnetArn"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetArns) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetArns:
    return list(data)
