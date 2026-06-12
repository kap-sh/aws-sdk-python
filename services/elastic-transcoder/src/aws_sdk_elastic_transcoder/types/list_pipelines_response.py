"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListPipelinesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.pipelines


class ListPipelinesResponse(TypedDict):
    pipelines: NotRequired["aws_sdk_elastic_transcoder.types.pipelines.Pipelines"]
    """<p>An array of <code>Pipeline</code> objects.</p>"""
    next_page_token: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p>A value that you use to access the second and subsequent pages of results, if any. When the pipelines fit on one page or when you've reached the last page of results, the value of <code>NextPageToken</code> is <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelinesResponse) -> dict:
    out: dict = {}
    if "pipelines" in value:
        import aws_sdk_elastic_transcoder.types.pipelines

        out["Pipelines"] = aws_sdk_elastic_transcoder.types.pipelines.serialize_json(
            value["pipelines"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_json(data: dict) -> ListPipelinesResponse:
    out: ListPipelinesResponse = {}  # type: ignore[typeddict-item]
    if "Pipelines" in data:
        import aws_sdk_elastic_transcoder.types.pipelines

        out["pipelines"] = aws_sdk_elastic_transcoder.types.pipelines.deserialize_json(
            data["Pipelines"]
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
