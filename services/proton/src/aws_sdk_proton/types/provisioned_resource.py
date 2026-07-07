"""Generated from Smithy shape ``com.amazonaws.proton#ProvisionedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.provisioned_resource_engine
    import aws_sdk_proton.types.provisioned_resource_identifier
    import aws_sdk_proton.types.provisioned_resource_name


class ProvisionedResource(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_proton.types.provisioned_resource_name.ProvisionedResourceName"
    ]
    """<p>The provisioned resource name.</p>"""
    identifier: NotRequired[
        "aws_sdk_proton.types.provisioned_resource_identifier.ProvisionedResourceIdentifier"
    ]
    """<p>The provisioned resource identifier.</p>"""
    provisioning_engine: NotRequired[
        "aws_sdk_proton.types.provisioned_resource_engine.ProvisionedResourceEngine"
    ]
    r"""<p>The resource provisioning engine. At this time, <code>CLOUDFORMATION</code> can be used for Amazon Web Services-managed provisioning, and <code>TERRAFORM</code> can be used for self-managed provisioning.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "provisioning_engine" in value:
        out["provisioningEngine"] = value["provisioning_engine"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedResource:
    out: ProvisionedResource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "provisioningEngine" in data:
        out["provisioning_engine"] = data["provisioningEngine"]
    return out
