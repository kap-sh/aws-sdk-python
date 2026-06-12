"""Generated from Smithy shape ``com.amazonaws.connectcases#GetTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.created_time
    import aws_sdk_connectcases.types.deleted
    import aws_sdk_connectcases.types.last_modified_time
    import aws_sdk_connectcases.types.layout_configuration
    import aws_sdk_connectcases.types.required_field_list
    import aws_sdk_connectcases.types.tag_propagation_configuration_list
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.template_arn
    import aws_sdk_connectcases.types.template_case_rule_list
    import aws_sdk_connectcases.types.template_description
    import aws_sdk_connectcases.types.template_id
    import aws_sdk_connectcases.types.template_name
    import aws_sdk_connectcases.types.template_status


class GetTemplateResponse(TypedDict):
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    template_arn: "aws_sdk_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: "aws_sdk_connectcases.types.template_name.TemplateName"
    """<p>The name of the template.</p>"""
    description: NotRequired[
        "aws_sdk_connectcases.types.template_description.TemplateDescription"
    ]
    """<p>A brief description of the template.</p>"""
    layout_configuration: NotRequired[
        "aws_sdk_connectcases.types.layout_configuration.LayoutConfiguration"
    ]
    """<p>Configuration of layouts associated to the template.</p>"""
    required_fields: NotRequired[
        "aws_sdk_connectcases.types.required_field_list.RequiredFieldList"
    ]
    """<p>A list of fields that must contain a value for a case to be successfully created with this template.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    status: "aws_sdk_connectcases.types.template_status.TemplateStatus"
    """<p>The status of the template.</p>"""
    deleted: "aws_sdk_connectcases.types.deleted.Deleted"
    """<p>Denotes whether or not the resource has been deleted.</p>"""
    created_time: NotRequired["aws_sdk_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp at which the resource was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp at which the resource was created or last modified.</p>"""
    rules: NotRequired[
        "aws_sdk_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
    ]
    """<p>A list of case rules (also known as <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">case field conditions</a>) on a template. </p>"""
    tag_propagation_configurations: NotRequired[
        "aws_sdk_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateResponse) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "layout_configuration" in value:
        import aws_sdk_connectcases.types.layout_configuration

        out["layoutConfiguration"] = (
            aws_sdk_connectcases.types.layout_configuration.serialize_json(
                value["layout_configuration"]
            )
        )
    if "required_fields" in value:
        import aws_sdk_connectcases.types.required_field_list

        out["requiredFields"] = (
            aws_sdk_connectcases.types.required_field_list.serialize_json(
                value["required_fields"]
            )
        )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    out["status"] = value["status"]
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import aws_sdk_connectcases.types.created_time

        out["createdTime"] = aws_sdk_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            aws_sdk_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
    if "rules" in value:
        import aws_sdk_connectcases.types.template_case_rule_list

        out["rules"] = (
            aws_sdk_connectcases.types.template_case_rule_list.serialize_json(
                value["rules"]
            )
        )
    if "tag_propagation_configurations" in value:
        import aws_sdk_connectcases.types.tag_propagation_configuration_list

        out["tagPropagationConfigurations"] = (
            aws_sdk_connectcases.types.tag_propagation_configuration_list.serialize_json(
                value["tag_propagation_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemplateResponse:
    out: GetTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("GetTemplateResponse.template_id required")
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("GetTemplateResponse.template_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTemplateResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "layoutConfiguration" in data:
        import aws_sdk_connectcases.types.layout_configuration

        out["layout_configuration"] = (
            aws_sdk_connectcases.types.layout_configuration.deserialize_json(
                data["layoutConfiguration"]
            )
        )
    if "requiredFields" in data:
        import aws_sdk_connectcases.types.required_field_list

        out["required_fields"] = (
            aws_sdk_connectcases.types.required_field_list.deserialize_json(
                data["requiredFields"]
            )
        )
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetTemplateResponse.status required")
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if "createdTime" in data:
        import aws_sdk_connectcases.types.created_time

        out["created_time"] = aws_sdk_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if "lastModifiedTime" in data:
        import aws_sdk_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "rules" in data:
        import aws_sdk_connectcases.types.template_case_rule_list

        out["rules"] = (
            aws_sdk_connectcases.types.template_case_rule_list.deserialize_json(
                data["rules"]
            )
        )
    if "tagPropagationConfigurations" in data:
        import aws_sdk_connectcases.types.tag_propagation_configuration_list

        out["tag_propagation_configurations"] = (
            aws_sdk_connectcases.types.tag_propagation_configuration_list.deserialize_json(
                data["tagPropagationConfigurations"]
            )
        )
    return out
