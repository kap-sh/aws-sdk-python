"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_status
    import aws_sdk_cleanroomsml.types.uuid


class ListTrainedModelVersionsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The pagination token from a previous <code>ListTrainedModelVersions</code> request. Use this token to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum number of trained model versions to return in a single page. The default value is 10, and the maximum value is 100.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership identifier for the collaboration that contains the trained model.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model for which to list versions.</p>"""
    status: NotRequired[
        "aws_sdk_cleanroomsml.types.trained_model_status.TrainedModelStatus"
    ]
    """<p>Filter the results to only include trained model versions with the specified status. Valid values include <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>ACTIVE</code>, <code>CREATE_FAILED</code>, and others.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrainedModelVersionsRequest:
    out: ListTrainedModelVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
