"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_summary_list


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: "aws_sdk_bedrock_agentcore_control.types.dataset_summary_list.DatasetSummaryList"
    """<p> The list of datasets. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.dataset_summary_list

    out["datasets"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_summary_list.serialize_json(
            value["datasets"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "datasets" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_summary_list

        out["datasets"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_summary_list.deserialize_json(
                data["datasets"]
            )
        )
    else:
        raise DeserializationError("ListDatasetsResponse.datasets required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
