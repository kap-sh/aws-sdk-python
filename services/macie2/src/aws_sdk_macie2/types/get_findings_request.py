"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.sort_criteria


class GetFindingsRequest(TypedDict, closed=True):
    finding_ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of strings that lists the unique identifiers for the findings to retrieve. You can specify as many as 50 unique identifiers in this array.</p>"""
    sort_criteria: NotRequired["aws_sdk_macie2.types.sort_criteria.SortCriteria"]
    """<p>The criteria for sorting the results of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsRequest) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["findingIds"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["finding_ids"]
        )
    if "sort_criteria" in value:
        import aws_sdk_macie2.types.sort_criteria

        out["sortCriteria"] = aws_sdk_macie2.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsRequest:
    out: GetFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["finding_ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["findingIds"]
        )
    if "sortCriteria" in data:
        import aws_sdk_macie2.types.sort_criteria

        out["sort_criteria"] = aws_sdk_macie2.types.sort_criteria.deserialize_json(
            data["sortCriteria"]
        )
    return out
