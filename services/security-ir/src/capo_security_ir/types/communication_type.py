"""Generated from Smithy shape ``com.amazonaws.securityir#CommunicationType``."""

from typing import Literal, TypeAlias, cast

CommunicationType: TypeAlias = Literal[
    "Case Created",
    "Case Updated",
    "Case Acknowledged",
    "Case Closed",
    "Case Updated To Service Managed",
    "Case Status Updated",
    "Case Pending Customer Action Reminder",
    "Case Attachment Url Uploaded",
    "Case Comment Added",
    "Case Comment Updated",
    "Membership Created",
    "Membership Updated",
    "Membership Cancelled",
    "Register Delegated Administrator",
    "Deregister Delegated Administrator",
    "Disable AWS Service Access",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationType) -> str:
    return value


def deserialize_json(data: str) -> CommunicationType:
    return cast(CommunicationType, data)
