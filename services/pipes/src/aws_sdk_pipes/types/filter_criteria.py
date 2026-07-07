"""Generated from Smithy shape ``com.amazonaws.pipes#FilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.filter_list


class FilterCriteria(TypedDict, closed=True):
    filters: NotRequired["aws_sdk_pipes.types.filter_list.FilterList"]
    """<p>The event patterns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_pipes.types.filter_list

        out["Filters"] = aws_sdk_pipes.types.filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_pipes.types.filter_list

        out["filters"] = aws_sdk_pipes.types.filter_list.deserialize_json(
            data["Filters"]
        )
    return out
