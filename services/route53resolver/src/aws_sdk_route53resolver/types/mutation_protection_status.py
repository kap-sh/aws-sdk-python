"""Generated from Smithy shape ``com.amazonaws.route53resolver#MutationProtectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

MutationProtectionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: MutationProtectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MutationProtectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MutationProtectionStatus value: {data!r}")
    return cast(MutationProtectionStatus, data)
