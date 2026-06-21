"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the event category for which aggregation configuration is enabled. Valid value is Data.</p>"""
EventCategory: TypeAlias = Literal["insight",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventCategory:
    return cast(EventCategory, data)
