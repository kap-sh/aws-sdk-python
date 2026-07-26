"""Generated from Smithy shape ``com.amazonaws.iot#ListManagedJobTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.laser_max_results
    import capo_iot.types.managed_job_template_name
    import capo_iot.types.next_token


class ListManagedJobTemplatesRequest(TypedDict, closed=True):
    template_name: NotRequired[
        "capo_iot.types.managed_job_template_name.ManagedJobTemplateName"
    ]
    """<p>An optional parameter for template name. If specified, only the versions of the managed job templates that have the specified template name will be returned.</p>"""
    max_results: NotRequired["capo_iot.types.laser_max_results.LaserMaxResults"]
    """<p>Maximum number of entries that can be returned.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedJobTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedJobTemplatesRequest:
    out: ListManagedJobTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
