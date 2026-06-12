"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfNumberField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OcsfNumberField: TypeAlias = Literal[
    "activity_id",
    "compliance.status_id",
    "confidence_score",
    "severity_id",
    "status_id",
    "finding_info.related_events_count",
    "evidences.api.response.code",
    "evidences.dst_endpoint.autonomous_system.number",
    "evidences.dst_endpoint.port",
    "evidences.src_endpoint.autonomous_system.number",
    "evidences.src_endpoint.port",
    "resources.image.in_use_count",
    "vulnerabilities.cve.cvss.base_score",
    "vendor_attributes.severity_id",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activity_id",
        "compliance.status_id",
        "confidence_score",
        "severity_id",
        "status_id",
        "finding_info.related_events_count",
        "evidences.api.response.code",
        "evidences.dst_endpoint.autonomous_system.number",
        "evidences.dst_endpoint.port",
        "evidences.src_endpoint.autonomous_system.number",
        "evidences.src_endpoint.port",
        "resources.image.in_use_count",
        "vulnerabilities.cve.cvss.base_score",
        "vendor_attributes.severity_id",
    )
)


def serialize_json(value: OcsfNumberField) -> str:
    return value


def deserialize_json(data: str) -> OcsfNumberField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OcsfNumberField value: {data!r}")
    return cast(OcsfNumberField, data)
