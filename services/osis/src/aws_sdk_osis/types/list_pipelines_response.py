"""Generated from Smithy shape ``com.amazonaws.osis#ListPipelinesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.next_token
    import aws_sdk_osis.types.pipeline_summary_list


class ListPipelinesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_osis.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    pipelines: NotRequired[
        "aws_sdk_osis.types.pipeline_summary_list.PipelineSummaryList"
    ]
    """<p>A list of all existing Data Prepper pipelines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelinesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "pipelines" in value:
        import aws_sdk_osis.types.pipeline_summary_list

        out["Pipelines"] = aws_sdk_osis.types.pipeline_summary_list.serialize_json(
            value["pipelines"]
        )
    return out


def deserialize_json(data: dict) -> ListPipelinesResponse:
    out: ListPipelinesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Pipelines" in data:
        import aws_sdk_osis.types.pipeline_summary_list

        out["pipelines"] = aws_sdk_osis.types.pipeline_summary_list.deserialize_json(
            data["Pipelines"]
        )
    return out
