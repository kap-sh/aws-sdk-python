"""Generated from Smithy shape ``com.amazonaws.batch#RetryAction``."""

from typing import Literal, TypeAlias, cast

RetryAction: TypeAlias = Literal[
    "RETRY",
    "EXIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetryAction) -> str:
    return value


def deserialize_json(data: str) -> RetryAction:
    return cast(RetryAction, data)
