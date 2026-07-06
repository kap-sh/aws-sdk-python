"""Generated from Smithy shape ``com.amazonaws.sesv2#ListResourceTenantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token


class ListResourceTenantsRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to list associated tenants for.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListResourceTenants</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListResourceTenants</code> to indicate the position in the list of resource tenants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTenantsRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTenantsRequest:
    out: ListResourceTenantsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListResourceTenantsRequest.resource_arn required")
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
