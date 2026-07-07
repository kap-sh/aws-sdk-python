"""Generated from Smithy shape ``com.amazonaws.connectcases#TemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.tag_propagation_configuration_list
    import aws_sdk_connectcases.types.template_arn
    import aws_sdk_connectcases.types.template_id
    import aws_sdk_connectcases.types.template_name
    import aws_sdk_connectcases.types.template_status


class TemplateSummary(TypedDict, closed=True):
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>The unique identifier for the template.</p>"""
    template_arn: "aws_sdk_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: "aws_sdk_connectcases.types.template_name.TemplateName"
    """<p>The template name.</p>"""
    status: "aws_sdk_connectcases.types.template_status.TemplateStatus"
    """<p>The status of the template.</p>"""
    tag_propagation_configurations: NotRequired[
        "aws_sdk_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    out["name"] = value["name"]
    out["status"] = value["status"]
    if "tag_propagation_configurations" in value:
        import aws_sdk_connectcases.types.tag_propagation_configuration_list

        out["tagPropagationConfigurations"] = (
            aws_sdk_connectcases.types.tag_propagation_configuration_list.serialize_json(
                value["tag_propagation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("TemplateSummary.template_id required")
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("TemplateSummary.template_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TemplateSummary.name required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("TemplateSummary.status required")
    if "tagPropagationConfigurations" in data:
        import aws_sdk_connectcases.types.tag_propagation_configuration_list

        out["tag_propagation_configurations"] = (
            aws_sdk_connectcases.types.tag_propagation_configuration_list.deserialize_json(
                data["tagPropagationConfigurations"]
            )
        )
    return out
