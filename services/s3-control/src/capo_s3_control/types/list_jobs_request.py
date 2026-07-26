"""Generated from Smithy shape ``com.amazonaws.s3control#ListJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.job_status_list
    import capo_s3_control.types.max_results
    import capo_s3_control.types.string_for_next_token


class ListJobsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>"""
    job_statuses: NotRequired["capo_s3_control.types.job_status_list.JobStatusList"]
    """<p>The <code>List Jobs</code> request returns jobs that match the statuses listed in this element.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.string_for_next_token.StringForNextToken"
    ]
    """<p>A pagination token to request the next page of results. Use the token that Amazon S3 returned in the <code>NextToken</code> element of the <code>ListJobsResult</code> from the previous <code>List Jobs</code> request.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of jobs that Amazon S3 will include in the <code>List Jobs</code> response. If there are more jobs than this number, the response will include a pagination token in the <code>NextToken</code> field to enable you to retrieve the next page of results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListJobsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListJobsRequest:
    out: ListJobsRequest = {}  # type: ignore[typeddict-item]
    return out
