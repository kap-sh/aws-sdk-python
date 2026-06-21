"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceSoftwareSetComplianceStatus``."""

from typing import Literal, TypeAlias, cast

DeviceSoftwareSetComplianceStatus: TypeAlias = Literal[
    "NONE",
    "COMPLIANT",
    "NOT_COMPLIANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSoftwareSetComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceSoftwareSetComplianceStatus:
    return cast(DeviceSoftwareSetComplianceStatus, data)
