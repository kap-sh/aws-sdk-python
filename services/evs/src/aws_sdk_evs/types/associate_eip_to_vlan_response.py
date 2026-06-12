"""Generated from Smithy shape ``com.amazonaws.evs#AssociateEipToVlanResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_evs.types.vlan

class AssociateEipToVlanResponse(TypedDict):
    vlan: NotRequired["aws_sdk_evs.types.vlan.Vlan"]

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateEipToVlanResponse) -> dict:
    out: dict = {}
    if "vlan" in value:
        import aws_sdk_evs.types.vlan
        out["vlan"] = aws_sdk_evs.types.vlan.serialize_aws_json_1_0(value["vlan"])
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateEipToVlanResponse:
    out: AssociateEipToVlanResponse = {}  # type: ignore[typeddict-item]
    if "vlan" in data:
        import aws_sdk_evs.types.vlan
        out["vlan"] = aws_sdk_evs.types.vlan.deserialize_aws_json_1_0(data["vlan"])
    return out