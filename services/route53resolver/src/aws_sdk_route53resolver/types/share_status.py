"""Generated from Smithy shape ``com.amazonaws.route53resolver#ShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ShareStatus: TypeAlias = Literal[
    "NOT_SHARED",
    "SHARED_WITH_ME",
    "SHARED_BY_ME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_SHARED",
        "SHARED_WITH_ME",
        "SHARED_BY_ME",
    )
)


def serialize_aws_json_1_1(value: ShareStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatus value: {data!r}")
    return cast(ShareStatus, data)
