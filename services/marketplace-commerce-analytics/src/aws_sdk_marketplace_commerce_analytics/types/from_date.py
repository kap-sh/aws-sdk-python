"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#FromDate``."""

import datetime
from typing import TypeAlias

FromDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FromDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> FromDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
