"""Generated from Smithy shape ``com.amazonaws.budgets#GenericTimestamp``."""

import datetime
from typing import TypeAlias

"""<p> A generic time stamp. In Java, it's transformed to a <code>Date</code> object.</p>"""
GenericTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenericTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> GenericTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
