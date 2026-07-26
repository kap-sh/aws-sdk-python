"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ExpirationTimestamp``."""

import datetime
from typing import TypeAlias

ExpirationTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpirationTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ExpirationTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
