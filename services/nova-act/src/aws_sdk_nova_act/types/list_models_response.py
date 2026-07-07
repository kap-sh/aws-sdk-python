"""Generated from Smithy shape ``com.amazonaws.novaact#ListModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.compatibility_information
    import aws_sdk_nova_act.types.model_aliases
    import aws_sdk_nova_act.types.model_summaries


class ListModelsResponse(TypedDict, closed=True):
    model_summaries: "aws_sdk_nova_act.types.model_summaries.ModelSummaries"
    """<p>A list of available AI models with their status and compatibility information.</p>"""
    model_aliases: "aws_sdk_nova_act.types.model_aliases.ModelAliases"
    """<p>A list of model aliases that provide stable references to model versions.</p>"""
    compatibility_information: (
        "aws_sdk_nova_act.types.compatibility_information.CompatibilityInformation"
    )
    """<p>Information about client compatibility and supported models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.model_summaries

    out["modelSummaries"] = aws_sdk_nova_act.types.model_summaries.serialize_json(
        value["model_summaries"]
    )
    import aws_sdk_nova_act.types.model_aliases

    out["modelAliases"] = aws_sdk_nova_act.types.model_aliases.serialize_json(
        value["model_aliases"]
    )
    import aws_sdk_nova_act.types.compatibility_information

    out["compatibilityInformation"] = (
        aws_sdk_nova_act.types.compatibility_information.serialize_json(
            value["compatibility_information"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListModelsResponse:
    out: ListModelsResponse = {}  # type: ignore[typeddict-item]
    if "modelSummaries" in data:
        import aws_sdk_nova_act.types.model_summaries

        out["model_summaries"] = (
            aws_sdk_nova_act.types.model_summaries.deserialize_json(
                data["modelSummaries"]
            )
        )
    else:
        raise DeserializationError("ListModelsResponse.model_summaries required")
    if "modelAliases" in data:
        import aws_sdk_nova_act.types.model_aliases

        out["model_aliases"] = aws_sdk_nova_act.types.model_aliases.deserialize_json(
            data["modelAliases"]
        )
    else:
        raise DeserializationError("ListModelsResponse.model_aliases required")
    if "compatibilityInformation" in data:
        import aws_sdk_nova_act.types.compatibility_information

        out["compatibility_information"] = (
            aws_sdk_nova_act.types.compatibility_information.deserialize_json(
                data["compatibilityInformation"]
            )
        )
    else:
        raise DeserializationError(
            "ListModelsResponse.compatibility_information required"
        )
    return out
