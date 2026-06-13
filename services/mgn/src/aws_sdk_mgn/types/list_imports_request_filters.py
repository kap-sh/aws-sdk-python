"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportsRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_i_ds_filter


class ListImportsRequestFilters(TypedDict):
    import_i_ds: NotRequired["aws_sdk_mgn.types.import_i_ds_filter.ImportIDsFilter"]
    """<p>List imports request filters import IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsRequestFilters) -> dict:
    out: dict = {}
    if "import_i_ds" in value:
        import aws_sdk_mgn.types.import_i_ds_filter

        out["importIDs"] = aws_sdk_mgn.types.import_i_ds_filter.serialize_json(
            value["import_i_ds"]
        )
    return out


def deserialize_json(data: dict) -> ListImportsRequestFilters:
    out: ListImportsRequestFilters = {}  # type: ignore[typeddict-item]
    if "importIDs" in data:
        import aws_sdk_mgn.types.import_i_ds_filter

        out["import_i_ds"] = aws_sdk_mgn.types.import_i_ds_filter.deserialize_json(
            data["importIDs"]
        )
    return out
