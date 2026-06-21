"""Generated from Smithy shape ``com.amazonaws.guardduty#PublishingStatus``."""

from typing import Literal, TypeAlias, cast

PublishingStatus: TypeAlias = Literal[
    "PENDING_VERIFICATION",
    "PUBLISHING",
    "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublishingStatus) -> str:
    return value


def deserialize_json(data: str) -> PublishingStatus:
    return cast(PublishingStatus, data)
