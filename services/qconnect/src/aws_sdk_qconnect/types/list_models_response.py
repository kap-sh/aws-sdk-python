"""Generated from Smithy shape ``com.amazonaws.qconnect#ListModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.model_summary_list
    import aws_sdk_qconnect.types.next_token


class ListModelsResponse(TypedDict, closed=True):
    model_summaries: "aws_sdk_qconnect.types.model_summary_list.ModelSummaryList"
    """<p>The summaries of the models available to the assistant.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.model_summary_list

    out["modelSummaries"] = aws_sdk_qconnect.types.model_summary_list.serialize_json(
        value["model_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListModelsResponse:
    out: ListModelsResponse = {}  # type: ignore[typeddict-item]
    if "modelSummaries" in data:
        import aws_sdk_qconnect.types.model_summary_list

        out["model_summaries"] = (
            aws_sdk_qconnect.types.model_summary_list.deserialize_json(
                data["modelSummaries"]
            )
        )
    else:
        raise DeserializationError("ListModelsResponse.model_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
