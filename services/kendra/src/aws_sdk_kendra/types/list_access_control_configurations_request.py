"""Generated from Smithy shape ``com.amazonaws.kendra#ListAccessControlConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.max_results_integer_for_list_access_control_configurations_request
    import aws_sdk_kendra.types.string


class ListAccessControlConfigurationsRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the access control configuration.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>If the previous response was incomplete (because there's more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of access control configurations.</p>"""
    max_results: NotRequired[
        "aws_sdk_kendra.types.max_results_integer_for_list_access_control_configurations_request.MaxResultsIntegerForListAccessControlConfigurationsRequest"
    ]
    """<p>The maximum number of access control configurations to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessControlConfigurationsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessControlConfigurationsRequest:
    out: ListAccessControlConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "ListAccessControlConfigurationsRequest.index_id required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
