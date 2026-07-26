"""Generated from Smithy shape ``com.amazonaws.emr#ListReleaseLabelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.max_results_number
    import capo_emr.types.release_label_filter
    import capo_emr.types.string


class ListReleaseLabelsInput(TypedDict, closed=True):
    filters: NotRequired["capo_emr.types.release_label_filter.ReleaseLabelFilter"]
    """<p>Filters the results of the request. <code>Prefix</code> specifies the prefix of release labels to return. <code>Application</code> specifies the application (with/without version) of release labels to return.</p>"""
    next_token: NotRequired["capo_emr.types.string.String"]
    """<p>Specifies the next page of results. If <code>NextToken</code> is not specified, which is usually the case for the first request of ListReleaseLabels, the first page of results are determined by other filtering parameters or by the latest version. The <code>ListReleaseLabels</code> request fails if the identity (Amazon Web Services account ID) and all filtering parameters are different from the original request, or if the <code>NextToken</code> is expired or tampered with.</p>"""
    max_results: NotRequired["capo_emr.types.max_results_number.MaxResultsNumber"]
    """<p>Defines the maximum number of release labels to return in a single response. The default is <code>100</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReleaseLabelsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_emr.types.release_label_filter

        out["Filters"] = capo_emr.types.release_label_filter.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReleaseLabelsInput:
    out: ListReleaseLabelsInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_emr.types.release_label_filter

        out["filters"] = capo_emr.types.release_label_filter.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
