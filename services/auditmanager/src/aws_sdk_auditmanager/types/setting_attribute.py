"""Generated from Smithy shape ``com.amazonaws.auditmanager#SettingAttribute``."""

from typing import Literal, TypeAlias, cast

SettingAttribute: TypeAlias = Literal[
    "ALL",
    "IS_AWS_ORG_ENABLED",
    "SNS_TOPIC",
    "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
    "DEFAULT_PROCESS_OWNERS",
    "EVIDENCE_FINDER_ENABLEMENT",
    "DEREGISTRATION_POLICY",
    "DEFAULT_EXPORT_DESTINATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SettingAttribute) -> str:
    return value


def deserialize_json(data: str) -> SettingAttribute:
    return cast(SettingAttribute, data)
