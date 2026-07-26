"""Generated from Smithy shape ``com.amazonaws.iot#ListProvisioningTemplateVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.template_name


class ListProvisioningTemplateVersionsRequest(TypedDict, closed=True):
    template_name: "capo_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisioningTemplateVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProvisioningTemplateVersionsRequest:
    out: ListProvisioningTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
