"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CustomOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_items
    import capo_bedrock_data_automation.types.document_custom_output_configuration


class CustomOutputConfiguration(TypedDict, closed=True):
    blueprints: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_items.BlueprintItems"
    ]
    document: NotRequired[
        "capo_bedrock_data_automation.types.document_custom_output_configuration.DocumentCustomOutputConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CustomOutputConfiguration) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import capo_bedrock_data_automation.types.blueprint_items

        out["blueprints"] = (
            capo_bedrock_data_automation.types.blueprint_items.serialize_json(
                value["blueprints"]
            )
        )
    if "document" in value:
        import capo_bedrock_data_automation.types.document_custom_output_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_custom_output_configuration.serialize_json(
                value["document"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOutputConfiguration:
    out: CustomOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("blueprints") is not None:
        import capo_bedrock_data_automation.types.blueprint_items

        out["blueprints"] = (
            capo_bedrock_data_automation.types.blueprint_items.deserialize_json(
                data["blueprints"]
            )
        )
    if data.get("document") is not None:
        import capo_bedrock_data_automation.types.document_custom_output_configuration

        out["document"] = (
            capo_bedrock_data_automation.types.document_custom_output_configuration.deserialize_json(
                data["document"]
            )
        )
    return out
