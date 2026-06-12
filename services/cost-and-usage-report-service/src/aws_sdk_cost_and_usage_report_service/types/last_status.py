"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#LastStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

LastStatus: TypeAlias = Literal[
    "SUCCESS",
    "ERROR_PERMISSIONS",
    "ERROR_NO_BUCKET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "ERROR_PERMISSIONS",
        "ERROR_NO_BUCKET",
    )
)


def serialize_aws_json_1_1(value: LastStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastStatus value: {data!r}")
    return cast(LastStatus, data)
