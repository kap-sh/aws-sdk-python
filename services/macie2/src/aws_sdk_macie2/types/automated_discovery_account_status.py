"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryAccountStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of automated sensitive data discovery for an Amazon Macie account. Valid values are:</p>"""
AutomatedDiscoveryAccountStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryAccountStatus:
    return cast(AutomatedDiscoveryAccountStatus, data)
