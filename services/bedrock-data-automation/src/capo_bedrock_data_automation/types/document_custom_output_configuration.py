"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentCustomOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.fallback_blueprint_items


class DocumentCustomOutputConfiguration(TypedDict, closed=True):
    fallback_blueprints: NotRequired[
        "capo_bedrock_data_automation.types.fallback_blueprint_items.FallbackBlueprintItems"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentCustomOutputConfiguration) -> dict:
    out: dict = {}
    if "fallback_blueprints" in value:
        import capo_bedrock_data_automation.types.fallback_blueprint_items

        out["fallbackBlueprints"] = (
            capo_bedrock_data_automation.types.fallback_blueprint_items.serialize_json(
                value["fallback_blueprints"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentCustomOutputConfiguration:
    out: DocumentCustomOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "fallbackBlueprints" in data:
        import capo_bedrock_data_automation.types.fallback_blueprint_items

        out["fallback_blueprints"] = (
            capo_bedrock_data_automation.types.fallback_blueprint_items.deserialize_json(
                data["fallbackBlueprints"]
            )
        )
    return out
