"""Generated from Smithy shape ``com.amazonaws.lambda#FilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.filter_list


class FilterCriteria(TypedDict, closed=True):
    filters: NotRequired["capo_lambda.types.filter_list.FilterList"]
    """<p> A list of filters. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_lambda.types.filter_list

        out["Filters"] = capo_lambda.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_lambda.types.filter_list

        out["filters"] = capo_lambda.types.filter_list.deserialize_json(data["Filters"])
    return out
