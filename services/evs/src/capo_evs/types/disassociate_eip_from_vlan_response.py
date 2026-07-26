"""Generated from Smithy shape ``com.amazonaws.evs#DisassociateEipFromVlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.vlan


class DisassociateEipFromVlanResponse(TypedDict, closed=True):
    vlan: NotRequired["capo_evs.types.vlan.Vlan"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateEipFromVlanResponse) -> dict:
    out: dict = {}
    if "vlan" in value:
        import capo_evs.types.vlan

        out["vlan"] = capo_evs.types.vlan.serialize_aws_json_1_0(value["vlan"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateEipFromVlanResponse:
    out: DisassociateEipFromVlanResponse = {}  # type: ignore[typeddict-item]
    if "vlan" in data:
        import capo_evs.types.vlan

        out["vlan"] = capo_evs.types.vlan.deserialize_aws_json_1_0(data["vlan"])
    return out
