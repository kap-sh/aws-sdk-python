"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

MetricsStatus: TypeAlias = Literal[
    "PUBLISH_SUCCEEDED",
    "PUBLISH_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISH_SUCCEEDED",
        "PUBLISH_FAILED",
    )
)


def serialize_json(value: MetricsStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricsStatus value: {data!r}")
    return cast(MetricsStatus, data)
