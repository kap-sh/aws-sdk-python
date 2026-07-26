"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.next_token
    import capo_sesv2.types.tenant_resource_list


class ListTenantResourcesResponse(TypedDict, closed=True):
    tenant_resources: NotRequired[
        "capo_sesv2.types.tenant_resource_list.TenantResourceList"
    ]
    """<p>An array that contains information about each resource associated with the tenant.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional resources to list. To view additional resources, issue another request to <code>ListTenantResources</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTenantResourcesResponse) -> dict:
    out: dict = {}
    if "tenant_resources" in value:
        import capo_sesv2.types.tenant_resource_list

        out["TenantResources"] = capo_sesv2.types.tenant_resource_list.serialize_json(
            value["tenant_resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTenantResourcesResponse:
    out: ListTenantResourcesResponse = {}  # type: ignore[typeddict-item]
    if "TenantResources" in data:
        import capo_sesv2.types.tenant_resource_list

        out["tenant_resources"] = (
            capo_sesv2.types.tenant_resource_list.deserialize_json(
                data["TenantResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
