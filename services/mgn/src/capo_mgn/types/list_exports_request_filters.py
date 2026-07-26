"""Generated from Smithy shape ``com.amazonaws.mgn#ListExportsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_exports_request_filters_export_i_ds


class ListExportsRequestFilters(TypedDict, closed=True):
    export_i_ds: NotRequired[
        "capo_mgn.types.list_exports_request_filters_export_i_ds.ListExportsRequestFiltersExportIDs"
    ]
    """<p>List exports request filters export ids.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsRequestFilters) -> dict:
    out: dict = {}
    if "export_i_ds" in value:
        import capo_mgn.types.list_exports_request_filters_export_i_ds

        out["exportIDs"] = (
            capo_mgn.types.list_exports_request_filters_export_i_ds.serialize_json(
                value["export_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListExportsRequestFilters:
    out: ListExportsRequestFilters = {}  # type: ignore[typeddict-item]
    if "exportIDs" in data:
        import capo_mgn.types.list_exports_request_filters_export_i_ds

        out["export_i_ds"] = (
            capo_mgn.types.list_exports_request_filters_export_i_ds.deserialize_json(
                data["exportIDs"]
            )
        )
    return out
