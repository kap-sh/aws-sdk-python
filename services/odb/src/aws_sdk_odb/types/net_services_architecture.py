"""Generated from Smithy shape ``com.amazonaws.odb#NetServicesArchitecture``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

NetServicesArchitecture: TypeAlias = Literal[
    "DEDICATED",
    "SHARED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEDICATED",
        "SHARED",
    )
)


def serialize_aws_json_1_0(value: NetServicesArchitecture) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetServicesArchitecture:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetServicesArchitecture value: {data!r}")
    return cast(NetServicesArchitecture, data)
