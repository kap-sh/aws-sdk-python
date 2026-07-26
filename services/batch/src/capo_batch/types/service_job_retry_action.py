"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobRetryAction``."""

from typing import Literal, TypeAlias, cast

ServiceJobRetryAction: TypeAlias = Literal[
    "RETRY",
    "EXIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobRetryAction) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobRetryAction:
    return cast(ServiceJobRetryAction, data)
