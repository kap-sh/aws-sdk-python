"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowRequestTimestamp``."""

import datetime
from typing import TypeAlias

FlowRequestTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowRequestTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> FlowRequestTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
