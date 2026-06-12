"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryMonitoringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies whether automated sensitive data discovery is currently configured to analyze objects in an S3 bucket. Possible values are:</p>"""
AutomatedDiscoveryMonitoringStatus: TypeAlias = Literal[
    "MONITORED",
    "NOT_MONITORED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MONITORED",
        "NOT_MONITORED",
    )
)


def serialize_json(value: AutomatedDiscoveryMonitoringStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryMonitoringStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedDiscoveryMonitoringStatus value: {data!r}"
        )
    return cast(AutomatedDiscoveryMonitoringStatus, data)
