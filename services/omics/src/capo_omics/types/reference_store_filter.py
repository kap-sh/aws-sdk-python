"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceStoreFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.reference_store_name


class ReferenceStoreFilter(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.reference_store_name.ReferenceStoreName"]
    """<p>The name to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceStoreFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "created_after" in value:
        import capo_omics.types._prelude.timestamp

        out["createdAfter"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_omics.types._prelude.timestamp

        out["createdBefore"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["created_before"]
        )
    return out


def deserialize_json(data: dict) -> ReferenceStoreFilter:
    out: ReferenceStoreFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "createdAfter" in data:
        import capo_omics.types._prelude.timestamp

        out["created_after"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["createdAfter"]
        )
    if "createdBefore" in data:
        import capo_omics.types._prelude.timestamp

        out["created_before"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["createdBefore"]
        )
    return out
