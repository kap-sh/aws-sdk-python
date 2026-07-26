"""Generated from Smithy shape ``com.amazonaws.s3control#ListJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_list_descriptor_list
    import capo_s3_control.types.string_for_next_token


class ListJobsResult(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_s3_control.types.string_for_next_token.StringForNextToken"
    ]
    """<p>If the <code>List Jobs</code> request produced more than the maximum number of results, you can pass this value into a subsequent <code>List Jobs</code> request in order to retrieve the next page of results.</p>"""
    jobs: NotRequired[
        "capo_s3_control.types.job_list_descriptor_list.JobListDescriptorList"
    ]
    """<p>The list of current jobs and jobs that have ended within the last 30 days.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListJobsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "jobs" in value:
        import capo_s3_control.types.job_list_descriptor_list

        capo_s3_control.types.job_list_descriptor_list.serialize_xml(
            value["jobs"], el, "Jobs"
        )


def deserialize_xml(el: Element) -> ListJobsResult:
    out: ListJobsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_jobs = el.find("Jobs")
    if child_jobs is not None:
        import capo_s3_control.types.job_list_descriptor_list

        out["jobs"] = capo_s3_control.types.job_list_descriptor_list.deserialize_xml(
            child_jobs
        )
    return out
