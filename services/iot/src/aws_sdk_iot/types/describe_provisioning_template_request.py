"""Generated from Smithy shape ``com.amazonaws.iot#DescribeProvisioningTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.template_name


class DescribeProvisioningTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProvisioningTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProvisioningTemplateRequest:
    out: DescribeProvisioningTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
