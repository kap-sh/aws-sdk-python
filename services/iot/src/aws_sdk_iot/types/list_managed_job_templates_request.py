"""Generated from Smithy shape ``com.amazonaws.iot#ListManagedJobTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.laser_max_results
    import aws_sdk_iot.types.managed_job_template_name
    import aws_sdk_iot.types.next_token


class ListManagedJobTemplatesRequest(TypedDict):
    template_name: NotRequired[
        "aws_sdk_iot.types.managed_job_template_name.ManagedJobTemplateName"
    ]
    """<p>An optional parameter for template name. If specified, only the versions of the managed job templates that have the specified template name will be returned.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.laser_max_results.LaserMaxResults"]
    """<p>Maximum number of entries that can be returned.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedJobTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedJobTemplatesRequest:
    out: ListManagedJobTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
