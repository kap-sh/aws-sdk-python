"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrincipalMatchOperator``."""

from typing import Literal, TypeAlias, cast

PrincipalMatchOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> PrincipalMatchOperator:
    return cast(PrincipalMatchOperator, data)
