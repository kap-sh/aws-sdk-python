"""Generated from Smithy shape ``com.amazonaws.medicalimaging#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.sort_field
    import capo_medical_imaging.types.sort_order


class Sort(TypedDict, closed=True):
    sort_order: "capo_medical_imaging.types.sort_order.SortOrder"
    """<p>The sort order for search criteria.</p>"""
    sort_field: "capo_medical_imaging.types.sort_field.SortField"
    """<p>The sort field for search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.sort_order

    out["sortOrder"] = capo_medical_imaging.types.sort_order.serialize_json(
        value["sort_order"]
    )
    import capo_medical_imaging.types.sort_field

    out["sortField"] = capo_medical_imaging.types.sort_field.serialize_json(
        value["sort_field"]
    )
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import capo_medical_imaging.types.sort_order

        out["sort_order"] = capo_medical_imaging.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        raise DeserializationError("Sort.sort_order required")
    if "sortField" in data:
        import capo_medical_imaging.types.sort_field

        out["sort_field"] = capo_medical_imaging.types.sort_field.deserialize_json(
            data["sortField"]
        )
    else:
        raise DeserializationError("Sort.sort_field required")
    return out
