"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ActorTokenContentType``."""

from typing import Literal, TypeAlias, cast

ActorTokenContentType: TypeAlias = Literal[
    "NONE",
    "M2M",
    "AWS_IAM_ID_TOKEN_JWT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActorTokenContentType) -> str:
    return value


def deserialize_json(data: str) -> ActorTokenContentType:
    return cast(ActorTokenContentType, data)
