"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.list_tenant_resources_filter
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.tenant_name


class ListTenantResourcesRequest(TypedDict):
    tenant_name: "aws_sdk_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to list resources for.</p>"""
    filter: NotRequired[
        "aws_sdk_sesv2.types.list_tenant_resources_filter.ListTenantResourcesFilter"
    ]
    """<p>A map of filter keys and values for filtering the list of tenant resources. Currently, the only supported filter key is <code>RESOURCE_TYPE</code>.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListTenantResources</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListTenantResources</code> to indicate the position in the list of tenant resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTenantResourcesRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    if "filter" in value:
        import aws_sdk_sesv2.types.list_tenant_resources_filter

        out["Filter"] = aws_sdk_sesv2.types.list_tenant_resources_filter.serialize_json(
            value["filter"]
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTenantResourcesRequest:
    out: ListTenantResourcesRequest = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    else:
        raise DeserializationError("ListTenantResourcesRequest.tenant_name required")
    if "Filter" in data:
        import aws_sdk_sesv2.types.list_tenant_resources_filter

        out["filter"] = (
            aws_sdk_sesv2.types.list_tenant_resources_filter.deserialize_json(
                data["Filter"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
