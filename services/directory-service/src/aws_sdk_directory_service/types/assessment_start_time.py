"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentStartTime``."""

import datetime
from typing import TypeAlias

AssessmentStartTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentStartTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> AssessmentStartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
