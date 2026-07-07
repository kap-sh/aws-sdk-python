"""Generated from Smithy shape ``com.amazonaws.location#CellSignals``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.lte_cell_details_list


class CellSignals(TypedDict, closed=True):
    lte_cell_details: "aws_sdk_location.types.lte_cell_details_list.LteCellDetailsList"
    """<p>Information about the Long-Term Evolution (LTE) network the device is connected to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellSignals) -> dict:
    out: dict = {}
    import aws_sdk_location.types.lte_cell_details_list

    out["LteCellDetails"] = aws_sdk_location.types.lte_cell_details_list.serialize_json(
        value["lte_cell_details"]
    )
    return out


def deserialize_json(data: dict) -> CellSignals:
    out: CellSignals = {}  # type: ignore[typeddict-item]
    if "LteCellDetails" in data:
        import aws_sdk_location.types.lte_cell_details_list

        out["lte_cell_details"] = (
            aws_sdk_location.types.lte_cell_details_list.deserialize_json(
                data["LteCellDetails"]
            )
        )
    else:
        raise DeserializationError("CellSignals.lte_cell_details required")
    return out
