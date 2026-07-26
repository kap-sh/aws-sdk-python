"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.earfcn
    import capo_iot_wireless.types.pci


class LteLocalId(TypedDict, closed=True):
    pci: "capo_iot_wireless.types.pci.PCI"
    """<p>Physical cell ID.</p>"""
    earfcn: "capo_iot_wireless.types.earfcn.EARFCN"
    """<p>Evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number (FCN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteLocalId) -> dict:
    out: dict = {}
    out["Pci"] = value["pci"]
    out["Earfcn"] = value["earfcn"]
    return out


def deserialize_json(data: dict) -> LteLocalId:
    out: LteLocalId = {}  # type: ignore[typeddict-item]
    if "Pci" in data:
        out["pci"] = data["Pci"]
    else:
        raise DeserializationError("LteLocalId.pci required")
    if "Earfcn" in data:
        out["earfcn"] = data["Earfcn"]
    else:
        raise DeserializationError("LteLocalId.earfcn required")
    return out
