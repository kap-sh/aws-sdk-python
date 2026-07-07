"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_version


class GetDatasetRequest(TypedDict, closed=True):
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset to retrieve. </p>"""
    dataset_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    ]
    r"""<p> Version to retrieve: \"DRAFT\" or a version number. Defaults to DRAFT if absent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDatasetRequest:
    out: GetDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
