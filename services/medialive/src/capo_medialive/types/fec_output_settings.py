"""Generated from Smithy shape ``com.amazonaws.medialive#FecOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max20
    import capo_medialive.types.__integer_min4_max20
    import capo_medialive.types.fec_output_include_fec


class FecOutputSettings(TypedDict, closed=True):
    column_depth: NotRequired[
        "capo_medialive.types.__integer_min4_max20.__integerMin4Max20"
    ]
    """Parameter D from SMPTE 2022-1. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet. Must be between 4 and 20, inclusive."""
    include_fec: NotRequired[
        "capo_medialive.types.fec_output_include_fec.FecOutputIncludeFec"
    ]
    """Enables column only or column and row based FEC"""
    row_length: NotRequired[
        "capo_medialive.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Parameter L from SMPTE 2022-1. The width of the FEC protection matrix. Must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness. If Row FEC is used, then this is the number of transport stream packets per row error correction packet, and the value must be between 4 and 20, inclusive, if includeFec is columnAndRow. If includeFec is column, this value must be 1 to 20, inclusive."""


# --- restJson1 ser/de ---
def serialize_json(value: FecOutputSettings) -> dict:
    out: dict = {}
    if "column_depth" in value:
        out["columnDepth"] = value["column_depth"]
    if "include_fec" in value:
        import capo_medialive.types.fec_output_include_fec

        out["includeFec"] = capo_medialive.types.fec_output_include_fec.serialize_json(
            value["include_fec"]
        )
    if "row_length" in value:
        out["rowLength"] = value["row_length"]
    return out


def deserialize_json(data: dict) -> FecOutputSettings:
    out: FecOutputSettings = {}  # type: ignore[typeddict-item]
    if "columnDepth" in data:
        out["column_depth"] = data["columnDepth"]
    if "includeFec" in data:
        import capo_medialive.types.fec_output_include_fec

        out["include_fec"] = (
            capo_medialive.types.fec_output_include_fec.deserialize_json(
                data["includeFec"]
            )
        )
    if "rowLength" in data:
        out["row_length"] = data["rowLength"]
    return out
