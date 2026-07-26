"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingAction``."""

from typing import Literal, TypeAlias, cast

ResponderErrorMaskingAction: TypeAlias = Literal[
    "NO_BID",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingAction) -> str:
    return value


def deserialize_json(data: str) -> ResponderErrorMaskingAction:
    return cast(ResponderErrorMaskingAction, data)
