"""Generated from Smithy shape ``com.amazonaws.datapipeline#ListPipelinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.string


class ListPipelinesInput(TypedDict, closed=True):
    marker: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>ListPipelines</code> with the marker value from the previous call to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesInput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesInput:
    out: ListPipelinesInput = {}  # type: ignore[typeddict-item]
    if "marker" in data:
        out["marker"] = data["marker"]
    return out
