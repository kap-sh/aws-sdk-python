"""Generated from Smithy shape ``com.amazonaws.transfer#MdnResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

MdnResponse: TypeAlias = Literal[
    "SYNC",
    "NONE",
    "ASYNC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYNC",
        "NONE",
        "ASYNC",
    )
)


def serialize_aws_json_1_1(value: MdnResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MdnResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MdnResponse value: {data!r}")
    return cast(MdnResponse, data)
