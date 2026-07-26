"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusReasonCode``."""

from typing import Literal, TypeAlias, cast

SchemaStatusReasonCode: TypeAlias = Literal[
    "ANALYSIS_RULE_MISSING",
    "ANALYSIS_TEMPLATES_NOT_CONFIGURED",
    "ANALYSIS_PROVIDERS_NOT_CONFIGURED",
    "DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED",
    "ID_MAPPING_TABLE_NOT_POPULATED",
    "COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED",
    "ADDITIONAL_ANALYSES_NOT_CONFIGURED",
    "RESULT_RECEIVERS_NOT_CONFIGURED",
    "ADDITIONAL_ANALYSES_NOT_ALLOWED",
    "RESULT_RECEIVERS_NOT_ALLOWED",
    "ANALYSIS_RULE_TYPES_NOT_COMPATIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> SchemaStatusReasonCode:
    return cast(SchemaStatusReasonCode, data)
