"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportDestinationType``."""

from typing import Literal, TypeAlias, cast

AssessmentReportDestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> AssessmentReportDestinationType:
    return cast(AssessmentReportDestinationType, data)
