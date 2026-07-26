"""Generated from Smithy shape ``com.amazonaws.iot#ListJobTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_template_summary_list
    import capo_iot.types.next_token


class ListJobTemplatesResponse(TypedDict, closed=True):
    job_templates: NotRequired[
        "capo_iot.types.job_template_summary_list.JobTemplateSummaryList"
    ]
    """<p>A list of objects that contain information about the job templates.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesResponse) -> dict:
    out: dict = {}
    if "job_templates" in value:
        import capo_iot.types.job_template_summary_list

        out["jobTemplates"] = capo_iot.types.job_template_summary_list.serialize_json(
            value["job_templates"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobTemplatesResponse:
    out: ListJobTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplates" in data:
        import capo_iot.types.job_template_summary_list

        out["job_templates"] = (
            capo_iot.types.job_template_summary_list.deserialize_json(
                data["jobTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
