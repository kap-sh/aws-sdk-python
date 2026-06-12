"""Generated from Smithy shape ``com.amazonaws.sesv2#ListResourceTenantsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.resource_tenant_metadata_list


class ListResourceTenantsResponse(TypedDict):
    resource_tenants: NotRequired[
        "aws_sdk_sesv2.types.resource_tenant_metadata_list.ResourceTenantMetadataList"
    ]
    """<p>An array that contains information about each tenant associated with the resource.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional tenants to list. To view additional tenants, issue another request to <code>ListResourceTenants</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTenantsResponse) -> dict:
    out: dict = {}
    if "resource_tenants" in value:
        import aws_sdk_sesv2.types.resource_tenant_metadata_list

        out["ResourceTenants"] = (
            aws_sdk_sesv2.types.resource_tenant_metadata_list.serialize_json(
                value["resource_tenants"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTenantsResponse:
    out: ListResourceTenantsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceTenants" in data:
        import aws_sdk_sesv2.types.resource_tenant_metadata_list

        out["resource_tenants"] = (
            aws_sdk_sesv2.types.resource_tenant_metadata_list.deserialize_json(
                data["ResourceTenants"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
