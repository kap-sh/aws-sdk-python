"""Generated from Smithy shape ``com.amazonaws.auditmanager#SettingAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "IS_AWS_ORG_ENABLED",
        "SNS_TOPIC",
        "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
        "DEFAULT_PROCESS_OWNERS",
        "EVIDENCE_FINDER_ENABLEMENT",
        "DEREGISTRATION_POLICY",
        "DEFAULT_EXPORT_DESTINATION",
    )
)


def serialize_json(value: SettingAttribute) -> str:
    return value


def deserialize_json(data: str) -> SettingAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SettingAttribute value: {data!r}")
    return cast(SettingAttribute, data)
