"""Generated from Smithy shape ``com.amazonaws.proton#CreateEnvironmentTemplateVersionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.template_version_source_input


class CreateEnvironmentTemplateVersionInput(TypedDict):
    client_token: NotRequired["aws_sdk_proton.types.client_token.ClientToken"]
    """<p>When included, if two identical requests are made with the same client token, Proton returns the environment template version that the first request created.</p>"""
    template_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    description: NotRequired["aws_sdk_proton.types.description.Description"]
    """<p>A description of the new version of an environment template.</p>"""
    major_version: NotRequired[
        "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>To create a new minor version of the environment template, include <code>major Version</code>.</p> <p>To create a new major and minor version of the environment template, exclude <code>major Version</code>.</p>"""
    source: (
        "aws_sdk_proton.types.template_version_source_input.TemplateVersionSourceInput"
    )
    """<p>An object that includes the template bundle S3 bucket path and name for the new version of an template.</p>"""
    tags: NotRequired["aws_sdk_proton.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the Proton environment template version. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentTemplateVersionInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["templateName"] = value["template_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "major_version" in value:
        out["majorVersion"] = value["major_version"]
    import aws_sdk_proton.types.template_version_source_input

    out["source"] = (
        aws_sdk_proton.types.template_version_source_input.serialize_aws_json_1_0(
            value["source"]
        )
    )
    if "tags" in value:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentTemplateVersionInput:
    out: CreateEnvironmentTemplateVersionInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "templateName" in data:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "CreateEnvironmentTemplateVersionInput.template_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "majorVersion" in data:
        out["major_version"] = data["majorVersion"]
    if "source" in data:
        import aws_sdk_proton.types.template_version_source_input

        out["source"] = (
            aws_sdk_proton.types.template_version_source_input.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentTemplateVersionInput.source required"
        )
    if "tags" in data:
        import aws_sdk_proton.types.tag_list

        out["tags"] = aws_sdk_proton.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
