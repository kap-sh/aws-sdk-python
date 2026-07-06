"""Generated from Smithy shape ``com.amazonaws.location#LteLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.earfcn
    import aws_sdk_location.types.pci


class LteLocalId(TypedDict, closed=True):
    earfcn: "aws_sdk_location.types.earfcn.Earfcn"
    """<p>E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).</p>"""
    pci: "aws_sdk_location.types.pci.Pci"
    """<p>Physical Cell ID (PCI).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteLocalId) -> dict:
    out: dict = {}
    out["Earfcn"] = value.get("earfcn", 0)
    out["Pci"] = value.get("pci", 0)
    return out


def deserialize_json(data: dict) -> LteLocalId:
    out: LteLocalId = {}  # type: ignore[typeddict-item]
    if "Earfcn" in data:
        out["earfcn"] = data["Earfcn"]
    else:
        out["earfcn"] = 0
    if "Pci" in data:
        out["pci"] = data["Pci"]
    else:
        out["pci"] = 0
    return out
