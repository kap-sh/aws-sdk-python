"""Generated from Smithy shape ``com.amazonaws.pi#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

FeatureStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "UNSUPPORTED",
    "ENABLED_PENDING_REBOOT",
    "DISABLED_PENDING_REBOOT",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "UNSUPPORTED",
        "ENABLED_PENDING_REBOOT",
        "DISABLED_PENDING_REBOOT",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: FeatureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureStatus value: {data!r}")
    return cast(FeatureStatus, data)
