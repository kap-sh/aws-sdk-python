"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameterDefaultValue``."""

import datetime
from typing import TypeAlias

"""<p>The default value for the date time parameter.</p>"""
DateTimeDatasetParameterDefaultValue: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameterDefaultValue) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DateTimeDatasetParameterDefaultValue:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
