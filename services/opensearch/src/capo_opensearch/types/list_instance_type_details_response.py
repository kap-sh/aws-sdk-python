"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInstanceTypeDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.instance_type_details_list
    import capo_opensearch.types.next_token


class ListInstanceTypeDetailsResponse(TypedDict, closed=True):
    instance_type_details: NotRequired[
        "capo_opensearch.types.instance_type_details_list.InstanceTypeDetailsList"
    ]
    """<p>Lists all supported instance types and features for the given OpenSearch or Elasticsearch version.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceTypeDetailsResponse) -> dict:
    out: dict = {}
    if "instance_type_details" in value:
        import capo_opensearch.types.instance_type_details_list

        out["InstanceTypeDetails"] = (
            capo_opensearch.types.instance_type_details_list.serialize_json(
                value["instance_type_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstanceTypeDetailsResponse:
    out: ListInstanceTypeDetailsResponse = {}  # type: ignore[typeddict-item]
    if "InstanceTypeDetails" in data:
        import capo_opensearch.types.instance_type_details_list

        out["instance_type_details"] = (
            capo_opensearch.types.instance_type_details_list.deserialize_json(
                data["InstanceTypeDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
