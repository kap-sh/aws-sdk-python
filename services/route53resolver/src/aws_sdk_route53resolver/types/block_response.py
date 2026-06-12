"""Generated from Smithy shape ``com.amazonaws.route53resolver#BlockResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

BlockResponse: TypeAlias = Literal[
    "NODATA",
    "NXDOMAIN",
    "OVERRIDE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NODATA",
        "NXDOMAIN",
        "OVERRIDE",
    )
)


def serialize_aws_json_1_1(value: BlockResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockResponse value: {data!r}")
    return cast(BlockResponse, data)
