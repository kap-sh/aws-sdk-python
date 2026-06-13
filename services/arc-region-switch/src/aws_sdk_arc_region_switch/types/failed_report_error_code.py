"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#FailedReportErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

FailedReportErrorCode: TypeAlias = Literal[
    "insufficientPermissions",
    "invalidResource",
    "configurationError",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "insufficientPermissions",
        "invalidResource",
        "configurationError",
    )
)


def serialize_aws_json_1_0(value: FailedReportErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailedReportErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailedReportErrorCode value: {data!r}")
    return cast(FailedReportErrorCode, data)
