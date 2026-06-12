"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.tenant_info_list


class ListTenantsResponse(TypedDict):
    tenants: NotRequired["aws_sdk_sesv2.types.tenant_info_list.TenantInfoList"]
    """<p>An array that contains basic information about each tenant.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional tenants to list. To view additional tenants, issue another request to <code>ListTenants</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTenantsResponse) -> dict:
    out: dict = {}
    if "tenants" in value:
        import aws_sdk_sesv2.types.tenant_info_list

        out["Tenants"] = aws_sdk_sesv2.types.tenant_info_list.serialize_json(
            value["tenants"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTenantsResponse:
    out: ListTenantsResponse = {}  # type: ignore[typeddict-item]
    if "Tenants" in data:
        import aws_sdk_sesv2.types.tenant_info_list

        out["tenants"] = aws_sdk_sesv2.types.tenant_info_list.deserialize_json(
            data["Tenants"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
