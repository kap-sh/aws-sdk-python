"""Generated from Smithy shape ``com.amazonaws.iot#DescribeManagedJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.managed_job_template_name
    import aws_sdk_iot.types.managed_template_version


class DescribeManagedJobTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_iot.types.managed_job_template_name.ManagedJobTemplateName"
    """<p>The unique name of a managed job template, which is required.</p>"""
    template_version: NotRequired[
        "aws_sdk_iot.types.managed_template_version.ManagedTemplateVersion"
    ]
    """<p>An optional parameter to specify version of a managed template. If not specified, the pre-defined default version is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeManagedJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeManagedJobTemplateRequest:
    out: DescribeManagedJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
