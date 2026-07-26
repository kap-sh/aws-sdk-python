"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolInstantiatedVnfInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.vnf_operational_state


class GetSolInstantiatedVnfInfo(TypedDict, closed=True):
    vnf_state: NotRequired["capo_tnb.types.vnf_operational_state.VnfOperationalState"]
    """<p>State of the network function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolInstantiatedVnfInfo) -> dict:
    out: dict = {}
    if "vnf_state" in value:
        import capo_tnb.types.vnf_operational_state

        out["vnfState"] = capo_tnb.types.vnf_operational_state.serialize_json(
            value["vnf_state"]
        )
    return out


def deserialize_json(data: dict) -> GetSolInstantiatedVnfInfo:
    out: GetSolInstantiatedVnfInfo = {}  # type: ignore[typeddict-item]
    if "vnfState" in data:
        import capo_tnb.types.vnf_operational_state

        out["vnf_state"] = capo_tnb.types.vnf_operational_state.deserialize_json(
            data["vnfState"]
        )
    return out
