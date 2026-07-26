"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.cell_params
    import capo_iot_wireless.types.uarfcn


class TdscdmaLocalId(TypedDict, closed=True):
    uarfcn: "capo_iot_wireless.types.uarfcn.UARFCN"
    """<p>TD-SCDMA UTRA (Universal Terrestrial Radio Access Network) absolute RF channel number (UARFCN).</p>"""
    cell_params: "capo_iot_wireless.types.cell_params.CellParams"
    """<p>Cell parameters for TD-SCDMA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaLocalId) -> dict:
    out: dict = {}
    out["Uarfcn"] = value["uarfcn"]
    out["CellParams"] = value["cell_params"]
    return out


def deserialize_json(data: dict) -> TdscdmaLocalId:
    out: TdscdmaLocalId = {}  # type: ignore[typeddict-item]
    if "Uarfcn" in data:
        out["uarfcn"] = data["Uarfcn"]
    else:
        raise DeserializationError("TdscdmaLocalId.uarfcn required")
    if "CellParams" in data:
        out["cell_params"] = data["CellParams"]
    else:
        raise DeserializationError("TdscdmaLocalId.cell_params required")
    return out
