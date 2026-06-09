"""Generated from Smithy shape ``com.amazonaws.eks#IpFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

IpFamily: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def serialize_json(value: IpFamily) -> str:
    return value


def deserialize_json(data: str) -> IpFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpFamily value: {data!r}")
    return cast(IpFamily, data)
