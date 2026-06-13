"""Generated from Smithy shape ``com.amazonaws.emr#LogUploadPolicyValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

LogUploadPolicyValue: TypeAlias = Literal[
    "emr-managed",
    "on-customer-s3only",
    "disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "emr-managed",
        "on-customer-s3only",
        "disabled",
    )
)


def serialize_aws_json_1_1(value: LogUploadPolicyValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogUploadPolicyValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogUploadPolicyValue value: {data!r}")
    return cast(LogUploadPolicyValue, data)
