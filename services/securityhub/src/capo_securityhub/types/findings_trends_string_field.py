"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsStringField``."""

from typing import Literal, TypeAlias, cast

FindingsTrendsStringField: TypeAlias = Literal[
    "account_id",
    "region",
    "finding_types",
    "finding_status",
    "finding_cve_ids",
    "finding_compliance_status",
    "finding_control_id",
    "finding_class_name",
    "finding_provider",
    "finding_activity_name",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsStringField) -> str:
    return value


def deserialize_json(data: str) -> FindingsTrendsStringField:
    return cast(FindingsTrendsStringField, data)
