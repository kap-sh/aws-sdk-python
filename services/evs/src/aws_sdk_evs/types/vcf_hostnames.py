"""Generated from Smithy shape ``com.amazonaws.evs#VcfHostnames``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.host_name


class VcfHostnames(TypedDict, closed=True):
    v_center: "aws_sdk_evs.types.host_name.HostName"
    """<p>The VMware vCenter hostname.</p>"""
    nsx: "aws_sdk_evs.types.host_name.HostName"
    """<p>The VMware NSX hostname.</p>"""
    nsx_manager1: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for the first VMware NSX Manager virtual machine (VM).</p>"""
    nsx_manager2: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for the second VMware NSX Manager virtual machine (VM).</p>"""
    nsx_manager3: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for the third VMware NSX Manager virtual machine (VM).</p>"""
    nsx_edge1: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for the first NSX Edge node.</p>"""
    nsx_edge2: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for the second NSX Edge node.</p>"""
    sddc_manager: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for SDDC Manager.</p>"""
    cloud_builder: "aws_sdk_evs.types.host_name.HostName"
    """<p>The hostname for VMware Cloud Builder.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VcfHostnames) -> dict:
    out: dict = {}
    out["vCenter"] = value["v_center"]
    out["nsx"] = value["nsx"]
    out["nsxManager1"] = value["nsx_manager1"]
    out["nsxManager2"] = value["nsx_manager2"]
    out["nsxManager3"] = value["nsx_manager3"]
    out["nsxEdge1"] = value["nsx_edge1"]
    out["nsxEdge2"] = value["nsx_edge2"]
    out["sddcManager"] = value["sddc_manager"]
    out["cloudBuilder"] = value["cloud_builder"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VcfHostnames:
    out: VcfHostnames = {}  # type: ignore[typeddict-item]
    if "vCenter" in data:
        out["v_center"] = data["vCenter"]
    else:
        raise DeserializationError("VcfHostnames.v_center required")
    if "nsx" in data:
        out["nsx"] = data["nsx"]
    else:
        raise DeserializationError("VcfHostnames.nsx required")
    if "nsxManager1" in data:
        out["nsx_manager1"] = data["nsxManager1"]
    else:
        raise DeserializationError("VcfHostnames.nsx_manager1 required")
    if "nsxManager2" in data:
        out["nsx_manager2"] = data["nsxManager2"]
    else:
        raise DeserializationError("VcfHostnames.nsx_manager2 required")
    if "nsxManager3" in data:
        out["nsx_manager3"] = data["nsxManager3"]
    else:
        raise DeserializationError("VcfHostnames.nsx_manager3 required")
    if "nsxEdge1" in data:
        out["nsx_edge1"] = data["nsxEdge1"]
    else:
        raise DeserializationError("VcfHostnames.nsx_edge1 required")
    if "nsxEdge2" in data:
        out["nsx_edge2"] = data["nsxEdge2"]
    else:
        raise DeserializationError("VcfHostnames.nsx_edge2 required")
    if "sddcManager" in data:
        out["sddc_manager"] = data["sddcManager"]
    else:
        raise DeserializationError("VcfHostnames.sddc_manager required")
    if "cloudBuilder" in data:
        out["cloud_builder"] = data["cloudBuilder"]
    else:
        raise DeserializationError("VcfHostnames.cloud_builder required")
    return out
