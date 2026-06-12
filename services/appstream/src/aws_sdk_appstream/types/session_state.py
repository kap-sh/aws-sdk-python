"""Generated from Smithy shape ``com.amazonaws.appstream#SessionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>Possible values for the state of a streaming session.</p>"""
SessionState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionState value: {data!r}")
    return cast(SessionState, data)
