"""Generated from Smithy shape ``com.amazonaws.fms#ListResourceSetResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.pagination_token
    import aws_sdk_fms.types.resource_list


class ListResourceSetResourcesResponse(TypedDict, closed=True):
    items: "aws_sdk_fms.types.resource_list.ResourceList"
    """<p>An array of the associated resources' uniform resource identifiers (URI).</p>"""
    next_token: NotRequired["aws_sdk_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceSetResourcesResponse) -> dict:
    out: dict = {}
    import aws_sdk_fms.types.resource_list

    out["Items"] = aws_sdk_fms.types.resource_list.serialize_aws_json_1_1(
        value["items"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceSetResourcesResponse:
    out: ListResourceSetResourcesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_fms.types.resource_list

        out["items"] = aws_sdk_fms.types.resource_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        raise DeserializationError("ListResourceSetResourcesResponse.items required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
