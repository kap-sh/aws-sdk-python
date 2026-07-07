"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of machine learning models. </p>"""
    model_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.model_summaries.ModelSummaries"
    ]
    """<p>Provides information on the specified model, including created time, model and dataset ARNs, and status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "model_summaries" in value:
        import aws_sdk_lookoutequipment.types.model_summaries

        out["ModelSummaries"] = (
            aws_sdk_lookoutequipment.types.model_summaries.serialize_aws_json_1_0(
                value["model_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListModelsResponse:
    out: ListModelsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ModelSummaries" in data:
        import aws_sdk_lookoutequipment.types.model_summaries

        out["model_summaries"] = (
            aws_sdk_lookoutequipment.types.model_summaries.deserialize_aws_json_1_0(
                data["ModelSummaries"]
            )
        )
    return out
