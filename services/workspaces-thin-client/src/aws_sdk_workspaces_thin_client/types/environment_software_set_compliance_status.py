"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#EnvironmentSoftwareSetComplianceStatus``."""

from typing import Literal, TypeAlias, cast

EnvironmentSoftwareSetComplianceStatus: TypeAlias = Literal[
    "NO_REGISTERED_DEVICES",
    "COMPLIANT",
    "NOT_COMPLIANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSoftwareSetComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentSoftwareSetComplianceStatus:
    return cast(EnvironmentSoftwareSetComplianceStatus, data)
