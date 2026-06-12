"""Generated from Smithy shape ``com.amazonaws.gamelift#IpProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

IpProtocol: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: IpProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpProtocol value: {data!r}")
    return cast(IpProtocol, data)
