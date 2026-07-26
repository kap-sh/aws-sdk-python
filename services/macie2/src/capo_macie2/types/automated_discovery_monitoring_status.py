"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryMonitoringStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether automated sensitive data discovery is currently configured to analyze objects in an S3 bucket. Possible values are:</p>"""
AutomatedDiscoveryMonitoringStatus: TypeAlias = Literal[
    "MONITORED",
    "NOT_MONITORED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryMonitoringStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryMonitoringStatus:
    return cast(AutomatedDiscoveryMonitoringStatus, data)
