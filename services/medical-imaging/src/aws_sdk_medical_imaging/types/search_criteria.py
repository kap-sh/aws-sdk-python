"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.search_filters
    import aws_sdk_medical_imaging.types.sort


class SearchCriteria(TypedDict):
    filters: NotRequired["aws_sdk_medical_imaging.types.search_filters.SearchFilters"]
    """<p>The filters for the search criteria.</p>"""
    sort: NotRequired["aws_sdk_medical_imaging.types.sort.Sort"]
    """<p>The sort input for search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCriteria) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_medical_imaging.types.search_filters

        out["filters"] = aws_sdk_medical_imaging.types.search_filters.serialize_json(
            value["filters"]
        )
    if "sort" in value:
        import aws_sdk_medical_imaging.types.sort

        out["sort"] = aws_sdk_medical_imaging.types.sort.serialize_json(value["sort"])
    return out


def deserialize_json(data: dict) -> SearchCriteria:
    out: SearchCriteria = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_medical_imaging.types.search_filters

        out["filters"] = aws_sdk_medical_imaging.types.search_filters.deserialize_json(
            data["filters"]
        )
    if "sort" in data:
        import aws_sdk_medical_imaging.types.sort

        out["sort"] = aws_sdk_medical_imaging.types.sort.deserialize_json(data["sort"])
    return out
