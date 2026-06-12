"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The type of data source of an export, can be one of the following:</p> <ul> <li> <p> <code>METRICS_DATA</code> - The metrics export.</p> </li> <li> <p> <code>MESSAGE_INSIGHTS</code> - The Message Insights export.</p> </li> </ul>"""
ExportSourceType: TypeAlias = Literal[
    "METRICS_DATA",
    "MESSAGE_INSIGHTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METRICS_DATA",
        "MESSAGE_INSIGHTS",
    )
)


def serialize_json(value: ExportSourceType) -> str:
    return value


def deserialize_json(data: str) -> ExportSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportSourceType value: {data!r}")
    return cast(ExportSourceType, data)
