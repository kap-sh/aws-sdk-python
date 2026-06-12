"""Generated from Smithy shape ``com.amazonaws.iot#ListProvisioningTemplateVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.template_name


class ListProvisioningTemplateVersionsRequest(TypedDict):
    template_name: "aws_sdk_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisioningTemplateVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProvisioningTemplateVersionsRequest:
    out: ListProvisioningTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
