"""Generated from Smithy shape ``com.amazonaws.acmpca#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER_ACCOUNTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "OTHER_ACCOUNTS",
    )
)


def serialize_aws_json_1_1(value: ResourceOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceOwner value: {data!r}")
    return cast(ResourceOwner, data)
