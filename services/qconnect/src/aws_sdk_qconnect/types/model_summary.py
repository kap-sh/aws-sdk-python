"""Generated from Smithy shape ``com.amazonaws.qconnect#ModelSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.ai_prompt_type_list
    import aws_sdk_qconnect.types.cross_region_status
    import aws_sdk_qconnect.types.model_display_name
    import aws_sdk_qconnect.types.model_id
    import aws_sdk_qconnect.types.model_lifecycle


class ModelSummary(TypedDict):
    model_id: "aws_sdk_qconnect.types.model_id.ModelId"
    """<p>The identifier of the model.</p>"""
    display_name: "aws_sdk_qconnect.types.model_display_name.ModelDisplayName"
    """<p>The display name of the model.</p>"""
    cross_region_status: NotRequired[
        "aws_sdk_qconnect.types.cross_region_status.CrossRegionStatus"
    ]
    """<p>The cross-region availability status of the model. <code>NONE</code> indicates the model is only available in a single region, <code>REGIONAL</code> indicates the model is available through regional inference, and <code>GLOBAL</code> indicates the model is available through global cross-region inference.</p>"""
    supports_prompt_caching: NotRequired["bool"]
    """<p>Whether the model supports prompt caching.</p>"""
    supported_ai_prompt_types: NotRequired[
        "aws_sdk_qconnect.types.ai_prompt_type_list.AIPromptTypeList"
    ]
    """<p>The list of AI Prompt types that the model supports.</p>"""
    model_lifecycle: NotRequired[
        "aws_sdk_qconnect.types.model_lifecycle.ModelLifecycle"
    ]
    """<p>The current lifecycle of the model. <code>ACTIVE</code> indicates the model is recommended for use and <code>LEGACY</code> indicates the model is still usable but is deprecated.</p>"""
    legacy_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the model lifecycle will transition from <code>ACTIVE</code> to <code>LEGACY</code>.</p>"""
    end_of_life_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the model will reach end of life and no longer be available for use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelSummary) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    out["displayName"] = value["display_name"]
    if "cross_region_status" in value:
        out["crossRegionStatus"] = value["cross_region_status"]
    if "supports_prompt_caching" in value:
        out["supportsPromptCaching"] = value["supports_prompt_caching"]
    if "supported_ai_prompt_types" in value:
        import aws_sdk_qconnect.types.ai_prompt_type_list

        out["supportedAIPromptTypes"] = (
            aws_sdk_qconnect.types.ai_prompt_type_list.serialize_json(
                value["supported_ai_prompt_types"]
            )
        )
    if "model_lifecycle" in value:
        out["modelLifecycle"] = value["model_lifecycle"]
    if "legacy_timestamp" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["legacyTimestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
                value["legacy_timestamp"]
            )
        )
    if "end_of_life_timestamp" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["endOfLifeTimestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
                value["end_of_life_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelSummary:
    out: ModelSummary = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("ModelSummary.model_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("ModelSummary.display_name required")
    if "crossRegionStatus" in data:
        out["cross_region_status"] = data["crossRegionStatus"]
    if "supportsPromptCaching" in data:
        out["supports_prompt_caching"] = data["supportsPromptCaching"]
    if "supportedAIPromptTypes" in data:
        import aws_sdk_qconnect.types.ai_prompt_type_list

        out["supported_ai_prompt_types"] = (
            aws_sdk_qconnect.types.ai_prompt_type_list.deserialize_json(
                data["supportedAIPromptTypes"]
            )
        )
    if "modelLifecycle" in data:
        out["model_lifecycle"] = data["modelLifecycle"]
    if "legacyTimestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["legacy_timestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["legacyTimestamp"]
            )
        )
    if "endOfLifeTimestamp" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["end_of_life_timestamp"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["endOfLifeTimestamp"]
            )
        )
    return out
