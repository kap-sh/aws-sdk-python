"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryAccountUpdateErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The error code that indicates why a request failed to change the status of automated sensitive data discovery for an Amazon Macie account. Possible values are:</p>"""
AutomatedDiscoveryAccountUpdateErrorCode: TypeAlias = Literal[
    "ACCOUNT_PAUSED",
    "ACCOUNT_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryAccountUpdateErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AutomatedDiscoveryAccountUpdateErrorCode:
    return cast(AutomatedDiscoveryAccountUpdateErrorCode, data)
