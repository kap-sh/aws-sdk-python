"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#RecommendationReportTimeStamp``."""

import datetime
from typing import TypeAlias

RecommendationReportTimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationReportTimeStamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> RecommendationReportTimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
