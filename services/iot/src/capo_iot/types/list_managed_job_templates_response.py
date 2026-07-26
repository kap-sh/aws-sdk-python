"""Generated from Smithy shape ``com.amazonaws.iot#ListManagedJobTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.managed_job_templates_summary_list
    import capo_iot.types.next_token


class ListManagedJobTemplatesResponse(TypedDict, closed=True):
    managed_job_templates: NotRequired[
        "capo_iot.types.managed_job_templates_summary_list.ManagedJobTemplatesSummaryList"
    ]
    """<p>A list of managed job templates that are returned.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedJobTemplatesResponse) -> dict:
    out: dict = {}
    if "managed_job_templates" in value:
        import capo_iot.types.managed_job_templates_summary_list

        out["managedJobTemplates"] = (
            capo_iot.types.managed_job_templates_summary_list.serialize_json(
                value["managed_job_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedJobTemplatesResponse:
    out: ListManagedJobTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "managedJobTemplates" in data:
        import capo_iot.types.managed_job_templates_summary_list

        out["managed_job_templates"] = (
            capo_iot.types.managed_job_templates_summary_list.deserialize_json(
                data["managedJobTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
