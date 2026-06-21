"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#MskEnhancedMonitoringLevel``."""

from typing import Literal, TypeAlias, cast

"""<p> Enumeration of supported enhanced monitoring levels for Amazon MSK clusters: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. </p>"""
MskEnhancedMonitoringLevel: TypeAlias = Literal[
    "DEFAULT",
    "PER_BROKER",
    "PER_TOPIC_PER_BROKER",
    "PER_TOPIC_PER_PARTITION",
]


# --- restJson1 ser/de ---
def serialize_json(value: MskEnhancedMonitoringLevel) -> str:
    return value


def deserialize_json(data: str) -> MskEnhancedMonitoringLevel:
    return cast(MskEnhancedMonitoringLevel, data)
