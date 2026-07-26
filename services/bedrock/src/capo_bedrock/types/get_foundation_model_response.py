"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.foundation_model_details


class GetFoundationModelResponse(TypedDict, closed=True):
    model_details: NotRequired[
        "capo_bedrock.types.foundation_model_details.FoundationModelDetails"
    ]
    """<p>Information about the foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelResponse) -> dict:
    out: dict = {}
    if "model_details" in value:
        import capo_bedrock.types.foundation_model_details

        out["modelDetails"] = (
            capo_bedrock.types.foundation_model_details.serialize_json(
                value["model_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFoundationModelResponse:
    out: GetFoundationModelResponse = {}  # type: ignore[typeddict-item]
    if "modelDetails" in data:
        import capo_bedrock.types.foundation_model_details

        out["model_details"] = (
            capo_bedrock.types.foundation_model_details.deserialize_json(
                data["modelDetails"]
            )
        )
    return out
