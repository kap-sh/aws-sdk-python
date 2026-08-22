"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PIIEntitiesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.pii_entity_types
    import capo_bedrock_data_automation.types.pii_redaction_mask_mode


class PIIEntitiesConfiguration(TypedDict, closed=True):
    pii_entity_types: NotRequired[
        "capo_bedrock_data_automation.types.pii_entity_types.PIIEntityTypes"
    ]
    """Types of PII entities to detect"""
    redaction_mask_mode: NotRequired[
        "capo_bedrock_data_automation.types.pii_redaction_mask_mode.PIIRedactionMaskMode"
    ]
    """Mode for redacting detected PII"""


# --- restJson1 ser/de ---
def serialize_json(value: PIIEntitiesConfiguration) -> dict:
    out: dict = {}
    if "pii_entity_types" in value:
        import capo_bedrock_data_automation.types.pii_entity_types

        out["piiEntityTypes"] = (
            capo_bedrock_data_automation.types.pii_entity_types.serialize_json(
                value["pii_entity_types"]
            )
        )
    if "redaction_mask_mode" in value:
        import capo_bedrock_data_automation.types.pii_redaction_mask_mode

        out["redactionMaskMode"] = (
            capo_bedrock_data_automation.types.pii_redaction_mask_mode.serialize_json(
                value["redaction_mask_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> PIIEntitiesConfiguration:
    out: PIIEntitiesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("piiEntityTypes") is not None:
        import capo_bedrock_data_automation.types.pii_entity_types

        out["pii_entity_types"] = (
            capo_bedrock_data_automation.types.pii_entity_types.deserialize_json(
                data["piiEntityTypes"]
            )
        )
    if data.get("redactionMaskMode") is not None:
        import capo_bedrock_data_automation.types.pii_redaction_mask_mode

        out["redaction_mask_mode"] = (
            capo_bedrock_data_automation.types.pii_redaction_mask_mode.deserialize_json(
                data["redactionMaskMode"]
            )
        )
    return out
