"""Generated from Smithy shape ``com.amazonaws.iot#DescribeProvisioningTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.template_name
    import aws_sdk_iot.types.template_version_id


class DescribeProvisioningTemplateVersionRequest(TypedDict, closed=True):
    template_name: "aws_sdk_iot.types.template_name.TemplateName"
    """<p>The template name.</p>"""
    version_id: "aws_sdk_iot.types.template_version_id.TemplateVersionId"
    """<p>The provisioning template version ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProvisioningTemplateVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProvisioningTemplateVersionRequest:
    out: DescribeProvisioningTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    return out
