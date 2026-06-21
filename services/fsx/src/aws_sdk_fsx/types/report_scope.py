"""Generated from Smithy shape ``com.amazonaws.fsx#ReportScope``."""

from typing import Literal, TypeAlias, cast

ReportScope: TypeAlias = Literal["FAILED_FILES_ONLY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportScope:
    return cast(ReportScope, data)
