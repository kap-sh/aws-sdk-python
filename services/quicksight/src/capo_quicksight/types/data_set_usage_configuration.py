"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetUsageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class DataSetUsageConfiguration(TypedDict, closed=True):
    disable_use_as_direct_query_source: "capo_quicksight.types.boolean.Boolean"
    """<p>An option that controls whether a child dataset of a direct query can use this dataset as a source.</p>"""
    disable_use_as_imported_source: "capo_quicksight.types.boolean.Boolean"
    """<p>An option that controls whether a child dataset that's stored in Quick Sight can use this dataset as a source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetUsageConfiguration) -> dict:
    out: dict = {}
    out["DisableUseAsDirectQuerySource"] = value.get(
        "disable_use_as_direct_query_source", False
    )
    out["DisableUseAsImportedSource"] = value.get(
        "disable_use_as_imported_source", False
    )
    return out


def deserialize_json(data: dict) -> DataSetUsageConfiguration:
    out: DataSetUsageConfiguration = {}  # type: ignore[typeddict-item]
    if "DisableUseAsDirectQuerySource" in data:
        out["disable_use_as_direct_query_source"] = data[
            "DisableUseAsDirectQuerySource"
        ]
    else:
        out["disable_use_as_direct_query_source"] = False
    if "DisableUseAsImportedSource" in data:
        out["disable_use_as_imported_source"] = data["DisableUseAsImportedSource"]
    else:
        out["disable_use_as_imported_source"] = False
    return out
