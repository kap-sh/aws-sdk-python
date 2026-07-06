"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_list_jobs_filter_term


class ListJobsFilterCriteria(TypedDict, closed=True):
    excludes: NotRequired[
        "aws_sdk_macie2.types.__list_of_list_jobs_filter_term.__listOfListJobsFilterTerm"
    ]
    """<p>An array of objects, one for each condition that determines which jobs to exclude from the results.</p>"""
    includes: NotRequired[
        "aws_sdk_macie2.types.__list_of_list_jobs_filter_term.__listOfListJobsFilterTerm"
    ]
    """<p>An array of objects, one for each condition that determines which jobs to include in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsFilterCriteria) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.__list_of_list_jobs_filter_term

        out["excludes"] = (
            aws_sdk_macie2.types.__list_of_list_jobs_filter_term.serialize_json(
                value["excludes"]
            )
        )
    if "includes" in value:
        import aws_sdk_macie2.types.__list_of_list_jobs_filter_term

        out["includes"] = (
            aws_sdk_macie2.types.__list_of_list_jobs_filter_term.serialize_json(
                value["includes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListJobsFilterCriteria:
    out: ListJobsFilterCriteria = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.__list_of_list_jobs_filter_term

        out["excludes"] = (
            aws_sdk_macie2.types.__list_of_list_jobs_filter_term.deserialize_json(
                data["excludes"]
            )
        )
    if "includes" in data:
        import aws_sdk_macie2.types.__list_of_list_jobs_filter_term

        out["includes"] = (
            aws_sdk_macie2.types.__list_of_list_jobs_filter_term.deserialize_json(
                data["includes"]
            )
        )
    return out
