"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_group_count


class GetFindingStatisticsResponse(TypedDict, closed=True):
    counts_by_group: NotRequired[
        "capo_macie2.types.__list_of_group_count.__listOfGroupCount"
    ]
    """<p>An array of objects, one for each group of findings that matches the filter criteria specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingStatisticsResponse) -> dict:
    out: dict = {}
    if "counts_by_group" in value:
        import capo_macie2.types.__list_of_group_count

        out["countsByGroup"] = capo_macie2.types.__list_of_group_count.serialize_json(
            value["counts_by_group"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingStatisticsResponse:
    out: GetFindingStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "countsByGroup" in data:
        import capo_macie2.types.__list_of_group_count

        out["counts_by_group"] = (
            capo_macie2.types.__list_of_group_count.deserialize_json(
                data["countsByGroup"]
            )
        )
    return out
