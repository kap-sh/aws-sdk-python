"""Generated from Smithy shape ``com.amazonaws.mgn#ListWavesRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.wave_i_ds_filter


class ListWavesRequestFilters(TypedDict, closed=True):
    wave_i_ds: NotRequired["aws_sdk_mgn.types.wave_i_ds_filter.WaveIDsFilter"]
    """<p>Filter waves list by wave ID.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Filter waves list by archival status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWavesRequestFilters) -> dict:
    out: dict = {}
    if "wave_i_ds" in value:
        import aws_sdk_mgn.types.wave_i_ds_filter

        out["waveIDs"] = aws_sdk_mgn.types.wave_i_ds_filter.serialize_json(
            value["wave_i_ds"]
        )
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    return out


def deserialize_json(data: dict) -> ListWavesRequestFilters:
    out: ListWavesRequestFilters = {}  # type: ignore[typeddict-item]
    if "waveIDs" in data:
        import aws_sdk_mgn.types.wave_i_ds_filter

        out["wave_i_ds"] = aws_sdk_mgn.types.wave_i_ds_filter.deserialize_json(
            data["waveIDs"]
        )
    if "isArchived" in data:
        out["is_archived"] = data["isArchived"]
    return out
