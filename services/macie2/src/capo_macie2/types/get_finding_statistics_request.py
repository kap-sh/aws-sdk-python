"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer
    import capo_macie2.types.finding_criteria
    import capo_macie2.types.finding_statistics_sort_criteria
    import capo_macie2.types.group_by


class GetFindingStatisticsRequest(TypedDict, closed=True):
    finding_criteria: NotRequired["capo_macie2.types.finding_criteria.FindingCriteria"]
    """<p>The criteria to use to filter the query results.</p>"""
    group_by: NotRequired["capo_macie2.types.group_by.GroupBy"]
    """<p>The finding property to use to group the query results. Valid values are:</p> <ul><li><p>classificationDetails.jobId - The unique identifier for the classification job that produced the finding.</p></li> <li><p>resourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.</p></li> <li><p>severity.description - The severity level of the finding, such as High or Medium.</p></li> <li><p>type - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.</p></li></ul>"""
    size: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    sort_criteria: NotRequired[
        "capo_macie2.types.finding_statistics_sort_criteria.FindingStatisticsSortCriteria"
    ]
    """<p>The criteria to use to sort the query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingStatisticsRequest) -> dict:
    out: dict = {}
    if "finding_criteria" in value:
        import capo_macie2.types.finding_criteria

        out["findingCriteria"] = capo_macie2.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "group_by" in value:
        import capo_macie2.types.group_by

        out["groupBy"] = capo_macie2.types.group_by.serialize_json(value["group_by"])
    if "size" in value:
        out["size"] = value["size"]
    if "sort_criteria" in value:
        import capo_macie2.types.finding_statistics_sort_criteria

        out["sortCriteria"] = (
            capo_macie2.types.finding_statistics_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFindingStatisticsRequest:
    out: GetFindingStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "findingCriteria" in data:
        import capo_macie2.types.finding_criteria

        out["finding_criteria"] = capo_macie2.types.finding_criteria.deserialize_json(
            data["findingCriteria"]
        )
    if "groupBy" in data:
        import capo_macie2.types.group_by

        out["group_by"] = capo_macie2.types.group_by.deserialize_json(data["groupBy"])
    if "size" in data:
        out["size"] = data["size"]
    if "sortCriteria" in data:
        import capo_macie2.types.finding_statistics_sort_criteria

        out["sort_criteria"] = (
            capo_macie2.types.finding_statistics_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
