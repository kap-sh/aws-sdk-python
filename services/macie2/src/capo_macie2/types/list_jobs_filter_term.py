"""Generated from Smithy shape ``com.amazonaws.macie2#ListJobsFilterTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.job_comparator
    import capo_macie2.types.list_jobs_filter_key


class ListJobsFilterTerm(TypedDict, closed=True):
    comparator: NotRequired["capo_macie2.types.job_comparator.JobComparator"]
    """<p>The operator to use to filter the results.</p>"""
    key: NotRequired["capo_macie2.types.list_jobs_filter_key.ListJobsFilterKey"]
    """<p>The property to use to filter the results.</p>"""
    values: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists one or more values to use to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsFilterTerm) -> dict:
    out: dict = {}
    if "comparator" in value:
        import capo_macie2.types.job_comparator

        out["comparator"] = capo_macie2.types.job_comparator.serialize_json(
            value["comparator"]
        )
    if "key" in value:
        import capo_macie2.types.list_jobs_filter_key

        out["key"] = capo_macie2.types.list_jobs_filter_key.serialize_json(value["key"])
    if "values" in value:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> ListJobsFilterTerm:
    out: ListJobsFilterTerm = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import capo_macie2.types.job_comparator

        out["comparator"] = capo_macie2.types.job_comparator.deserialize_json(
            data["comparator"]
        )
    if "key" in data:
        import capo_macie2.types.list_jobs_filter_key

        out["key"] = capo_macie2.types.list_jobs_filter_key.deserialize_json(
            data["key"]
        )
    if "values" in data:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["values"]
        )
    return out
