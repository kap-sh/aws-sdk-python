"""Generated from Smithy shape ``com.amazonaws.appstream#PreferredProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

PreferredProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "UDP",
    )
)


def serialize_aws_json_1_1(value: PreferredProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreferredProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreferredProtocol value: {data!r}")
    return cast(PreferredProtocol, data)
