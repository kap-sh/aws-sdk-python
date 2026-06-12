"""Generated from Smithy shape ``com.amazonaws.fsx#ReportScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

ReportScope: TypeAlias = Literal["FAILED_FILES_ONLY",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FAILED_FILES_ONLY",))


def serialize_aws_json_1_1(value: ReportScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportScope value: {data!r}")
    return cast(ReportScope, data)
