"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEntitlementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.vm_entitlement_list


class DeleteEntitlementResponse(TypedDict, closed=True):
    entitlements: NotRequired["aws_sdk_evs.types.vm_entitlement_list.VmEntitlementList"]
    """<p>A list of the deleted entitlements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEntitlementResponse) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_evs.types.vm_entitlement_list

        out["entitlements"] = (
            aws_sdk_evs.types.vm_entitlement_list.serialize_aws_json_1_0(
                value["entitlements"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEntitlementResponse:
    out: DeleteEntitlementResponse = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import aws_sdk_evs.types.vm_entitlement_list

        out["entitlements"] = (
            aws_sdk_evs.types.vm_entitlement_list.deserialize_aws_json_1_0(
                data["entitlements"]
            )
        )
    return out
