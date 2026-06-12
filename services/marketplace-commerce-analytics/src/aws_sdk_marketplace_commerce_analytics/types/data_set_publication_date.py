"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#DataSetPublicationDate``."""

import datetime
from typing import TypeAlias

DataSetPublicationDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSetPublicationDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> DataSetPublicationDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
