"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComplianceStatusType``."""

from typing import Literal, TypeAlias, cast

AppComplianceStatusType: TypeAlias = Literal[
    "PolicyBreached",
    "PolicyMet",
    "NotAssessed",
    "ChangesDetected",
    "NotApplicable",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppComplianceStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppComplianceStatusType:
    return cast(AppComplianceStatusType, data)
