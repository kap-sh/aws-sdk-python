"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelDealerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

IsraelDealerType: TypeAlias = Literal[
    "Authorized",
    "Non-authorized",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Authorized",
        "Non-authorized",
    )
)


def serialize_json(value: IsraelDealerType) -> str:
    return value


def deserialize_json(data: str) -> IsraelDealerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsraelDealerType value: {data!r}")
    return cast(IsraelDealerType, data)
