"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricNamespace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

MetricNamespace: TypeAlias = Literal["VDM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VDM",))


def serialize_json(value: MetricNamespace) -> str:
    return value


def deserialize_json(data: str) -> MetricNamespace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricNamespace value: {data!r}")
    return cast(MetricNamespace, data)
