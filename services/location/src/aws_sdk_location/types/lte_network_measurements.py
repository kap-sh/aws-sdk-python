"""Generated from Smithy shape ``com.amazonaws.location#LteNetworkMeasurements``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.earfcn
    import aws_sdk_location.types.eutran_cell_id
    import aws_sdk_location.types.pci
    import aws_sdk_location.types.rsrp
    import aws_sdk_location.types.rsrq


class LteNetworkMeasurements(TypedDict):
    earfcn: "aws_sdk_location.types.earfcn.Earfcn"
    """<p>E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).</p>"""
    cell_id: "aws_sdk_location.types.eutran_cell_id.EutranCellId"
    """<p>E-UTRAN Cell Identifier (ECI).</p>"""
    pci: "aws_sdk_location.types.pci.Pci"
    """<p>Physical Cell ID (PCI).</p>"""
    rsrp: NotRequired["aws_sdk_location.types.rsrp.Rsrp"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["aws_sdk_location.types.rsrq.Rsrq"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteNetworkMeasurements) -> dict:
    out: dict = {}
    out["Earfcn"] = value.get("earfcn", 0)
    out["CellId"] = value.get("cell_id", 0)
    out["Pci"] = value.get("pci", 0)
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = value["rsrq"]
    return out


def deserialize_json(data: dict) -> LteNetworkMeasurements:
    out: LteNetworkMeasurements = {}  # type: ignore[typeddict-item]
    if "Earfcn" in data:
        out["earfcn"] = data["Earfcn"]
    else:
        out["earfcn"] = 0
    if "CellId" in data:
        out["cell_id"] = data["CellId"]
    else:
        out["cell_id"] = 0
    if "Pci" in data:
        out["pci"] = data["Pci"]
    else:
        out["pci"] = 0
    if "Rsrp" in data:
        out["rsrp"] = data["Rsrp"]
    if "Rsrq" in data:
        out["rsrq"] = data["Rsrq"]
    return out
