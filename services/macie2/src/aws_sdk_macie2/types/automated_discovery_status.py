"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the automated sensitive data discovery configuration for an organization in Amazon Macie or a standalone Macie account. Valid values are:</p>"""
AutomatedDiscoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryStatus:
    return cast(AutomatedDiscoveryStatus, data)
