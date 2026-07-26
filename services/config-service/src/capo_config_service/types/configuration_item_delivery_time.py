"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItemDeliveryTime``."""

import datetime
from typing import TypeAlias

ConfigurationItemDeliveryTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItemDeliveryTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ConfigurationItemDeliveryTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
