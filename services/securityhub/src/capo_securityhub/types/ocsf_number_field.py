"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfNumberField``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: OcsfNumberField) -> str:
    return value


def deserialize_json(data: str) -> OcsfNumberField:
    return cast(OcsfNumberField, data)
