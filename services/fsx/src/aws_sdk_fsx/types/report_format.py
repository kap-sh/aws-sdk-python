"""Generated from Smithy shape ``com.amazonaws.fsx#ReportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

ReportFormat: TypeAlias = Literal["REPORT_CSV_20191124",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REPORT_CSV_20191124",))


def serialize_aws_json_1_1(value: ReportFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFormat value: {data!r}")
    return cast(ReportFormat, data)
