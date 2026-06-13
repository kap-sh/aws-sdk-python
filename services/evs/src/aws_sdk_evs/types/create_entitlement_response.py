"""Generated from Smithy shape ``com.amazonaws.evs#CreateEntitlementResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.vm_entitlement_list


class CreateEntitlementResponse(TypedDict):
    entitlements: NotRequired["aws_sdk_evs.types.vm_entitlement_list.VmEntitlementList"]
    """<p>A list of the created entitlements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEntitlementResponse) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_evs.types.vm_entitlement_list

        out["entitlements"] = (
            aws_sdk_evs.types.vm_entitlement_list.serialize_aws_json_1_0(
                value["entitlements"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEntitlementResponse:
    out: CreateEntitlementResponse = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import aws_sdk_evs.types.vm_entitlement_list

        out["entitlements"] = (
            aws_sdk_evs.types.vm_entitlement_list.deserialize_aws_json_1_0(
                data["entitlements"]
            )
        )
    return out
