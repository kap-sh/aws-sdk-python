"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.evidence_attribute_key
    import aws_sdk_auditmanager.types.evidence_attribute_value

EvidenceAttributes: TypeAlias = dict[
    "aws_sdk_auditmanager.types.evidence_attribute_key.EvidenceAttributeKey",
    "aws_sdk_auditmanager.types.evidence_attribute_value.EvidenceAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvidenceAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EvidenceAttributes:
    out: EvidenceAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
