"""Generated from Smithy shape ``com.amazonaws.bedrock#GetFoundationModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.foundation_model_details


class GetFoundationModelResponse(TypedDict, closed=True):
    model_details: NotRequired[
        "aws_sdk_bedrock.types.foundation_model_details.FoundationModelDetails"
    ]
    """<p>Information about the foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFoundationModelResponse) -> dict:
    out: dict = {}
    if "model_details" in value:
        import aws_sdk_bedrock.types.foundation_model_details

        out["modelDetails"] = (
            aws_sdk_bedrock.types.foundation_model_details.serialize_json(
                value["model_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFoundationModelResponse:
    out: GetFoundationModelResponse = {}  # type: ignore[typeddict-item]
    if "modelDetails" in data:
        import aws_sdk_bedrock.types.foundation_model_details

        out["model_details"] = (
            aws_sdk_bedrock.types.foundation_model_details.deserialize_json(
                data["modelDetails"]
            )
        )
    return out
