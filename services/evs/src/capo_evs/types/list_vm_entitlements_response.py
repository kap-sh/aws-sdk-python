"""Generated from Smithy shape ``com.amazonaws.evs#ListVmEntitlementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.pagination_token
    import capo_evs.types.vm_entitlement_list


class ListVmEntitlementsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    entitlements: NotRequired["capo_evs.types.vm_entitlement_list.VmEntitlementList"]
    """<p>A list of entitlements for virtual machines in the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVmEntitlementsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "entitlements" in value:
        import capo_evs.types.vm_entitlement_list

        out["entitlements"] = capo_evs.types.vm_entitlement_list.serialize_aws_json_1_0(
            value["entitlements"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVmEntitlementsResponse:
    out: ListVmEntitlementsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "entitlements" in data:
        import capo_evs.types.vm_entitlement_list

        out["entitlements"] = (
            capo_evs.types.vm_entitlement_list.deserialize_aws_json_1_0(
                data["entitlements"]
            )
        )
    return out
