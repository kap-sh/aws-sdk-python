"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.display_name
    import aws_sdk_proton.types.provisioning
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.tag_list


class CreateServiceTemplateInput(TypedDict):
    name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service template.</p>"""
    display_name: NotRequired["aws_sdk_proton.types.display_name.DisplayName"]
    """<p>The name of the service template as displayed in the developer interface.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>A description of the service template.</p>"""
    encryption_key: NotRequired["aws_sdk_proton.types.arn.Arn"]
    """<p>A customer provided encryption key that's used to encrypt data.</p>"""
    pipeline_provisioning: NotRequired["aws_sdk_proton.types.provisioning.Provisioning"]
    """<p>By default, Proton provides a service pipeline for your service. When this parameter is included, it indicates that an Proton service pipeline <i>isn't</i> provided for your service. After it's included, it <i>can't</i> be changed. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\">Template bundles</a> in the <i>Proton User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceTemplateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "pipeline_provisioning" in value:
        out["pipelineProvisioning"] = value["pipeline_provisioning"]
    if "tags" in value:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceTemplateInput:
    out: CreateServiceTemplateInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceTemplateInput.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "pipelineProvisioning" in data:
        out["pipeline_provisioning"] = data["pipelineProvisioning"]
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
