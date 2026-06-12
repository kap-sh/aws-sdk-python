"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItemCaptureTime``."""

import datetime
from typing import TypeAlias

ConfigurationItemCaptureTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItemCaptureTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ConfigurationItemCaptureTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
