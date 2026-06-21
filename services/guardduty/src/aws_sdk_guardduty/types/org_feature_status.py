"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeatureStatus``."""

from typing import Literal, TypeAlias, cast

OrgFeatureStatus: TypeAlias = Literal[
    "NEW",
    "NONE",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrgFeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> OrgFeatureStatus:
    return cast(OrgFeatureStatus, data)
