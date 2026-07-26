"""Generated from Smithy shape ``com.amazonaws.ecr#EvaluationTimestamp``."""

import datetime
from typing import TypeAlias

EvaluationTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EvaluationTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
