"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInstanceTypeDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.instance_type_details_list
    import aws_sdk_opensearch.types.next_token


class ListInstanceTypeDetailsResponse(TypedDict):
    instance_type_details: NotRequired[
        "aws_sdk_opensearch.types.instance_type_details_list.InstanceTypeDetailsList"
    ]
    """<p>Lists all supported instance types and features for the given OpenSearch or Elasticsearch version.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceTypeDetailsResponse) -> dict:
    out: dict = {}
    if "instance_type_details" in value:
        import aws_sdk_opensearch.types.instance_type_details_list

        out["InstanceTypeDetails"] = (
            aws_sdk_opensearch.types.instance_type_details_list.serialize_json(
                value["instance_type_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstanceTypeDetailsResponse:
    out: ListInstanceTypeDetailsResponse = {}  # type: ignore[typeddict-item]
    if "InstanceTypeDetails" in data:
        import aws_sdk_opensearch.types.instance_type_details_list

        out["instance_type_details"] = (
            aws_sdk_opensearch.types.instance_type_details_list.deserialize_json(
                data["InstanceTypeDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
