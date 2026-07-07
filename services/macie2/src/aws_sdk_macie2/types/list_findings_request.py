"""Generated from Smithy shape ``com.amazonaws.macie2#ListFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.finding_criteria
    import aws_sdk_macie2.types.sort_criteria


class ListFindingsRequest(TypedDict, closed=True):
    finding_criteria: NotRequired[
        "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
    ]
    """<p>The criteria to use to filter the results.</p>"""
    max_results: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_criteria: NotRequired["aws_sdk_macie2.types.sort_criteria.SortCriteria"]
    """<p>The criteria to use to sort the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsRequest) -> dict:
    out: dict = {}
    if "finding_criteria" in value:
        import aws_sdk_macie2.types.finding_criteria

        out["findingCriteria"] = aws_sdk_macie2.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_criteria" in value:
        import aws_sdk_macie2.types.sort_criteria

        out["sortCriteria"] = aws_sdk_macie2.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> ListFindingsRequest:
    out: ListFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingCriteria" in data:
        import aws_sdk_macie2.types.finding_criteria

        out["finding_criteria"] = (
            aws_sdk_macie2.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortCriteria" in data:
        import aws_sdk_macie2.types.sort_criteria

        out["sort_criteria"] = aws_sdk_macie2.types.sort_criteria.deserialize_json(
            data["sortCriteria"]
        )
    return out
