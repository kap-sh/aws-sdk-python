"""Generated from Smithy shape ``com.amazonaws.opensearch#SkipUnavailableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The status of <code>SkipUnavailable</code> setting for the outbound connection.</p> <ul> <li> <p> <b>ENABLED</b> - The <code>SkipUnavailable</code> setting is enabled for the connection.</p> </li> <li> <p> <b>DISABLED</b> - The <code>SkipUnavailable</code> setting is disabled for the connection.</p> </li> </ul>"""
SkipUnavailableStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: SkipUnavailableStatus) -> str:
    return value


def deserialize_json(data: str) -> SkipUnavailableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SkipUnavailableStatus value: {data!r}")
    return cast(SkipUnavailableStatus, data)
