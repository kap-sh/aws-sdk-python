"""Generated from Smithy shape ``com.amazonaws.location#CellSignals``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.lte_cell_details_list


class CellSignals(TypedDict, closed=True):
    lte_cell_details: "capo_location.types.lte_cell_details_list.LteCellDetailsList"
    """<p>Information about the Long-Term Evolution (LTE) network the device is connected to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellSignals) -> dict:
    out: dict = {}
    import capo_location.types.lte_cell_details_list

    out["LteCellDetails"] = capo_location.types.lte_cell_details_list.serialize_json(
        value["lte_cell_details"]
    )
    return out


def deserialize_json(data: dict) -> CellSignals:
    out: CellSignals = {}  # type: ignore[typeddict-item]
    if "LteCellDetails" in data:
        import capo_location.types.lte_cell_details_list

        out["lte_cell_details"] = (
            capo_location.types.lte_cell_details_list.deserialize_json(
                data["LteCellDetails"]
            )
        )
    else:
        raise DeserializationError("CellSignals.lte_cell_details required")
    return out
