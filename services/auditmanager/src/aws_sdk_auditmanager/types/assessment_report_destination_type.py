"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

AssessmentReportDestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: AssessmentReportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> AssessmentReportDestinationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssessmentReportDestinationType value: {data!r}"
        )
    return cast(AssessmentReportDestinationType, data)
