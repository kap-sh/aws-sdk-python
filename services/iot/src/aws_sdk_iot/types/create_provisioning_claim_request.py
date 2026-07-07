"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningClaimRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.template_name


class CreateProvisioningClaimRequest(TypedDict, closed=True):
    template_name: "aws_sdk_iot.types.template_name.TemplateName"
    """<p>The name of the provisioning template to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningClaimRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateProvisioningClaimRequest:
    out: CreateProvisioningClaimRequest = {}  # type: ignore[typeddict-item]
    return out
