"""Generated from Smithy shape ``com.amazonaws.directoryservice#EndDateTime``."""

import datetime
from typing import TypeAlias

EndDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EndDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
