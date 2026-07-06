"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.layout_configuration
    import aws_sdk_connectcases.types.required_field_list
    import aws_sdk_connectcases.types.tag_propagation_configuration_list
    import aws_sdk_connectcases.types.template_case_rule_list
    import aws_sdk_connectcases.types.template_description
    import aws_sdk_connectcases.types.template_name
    import aws_sdk_connectcases.types.template_status


class CreateTemplateRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    name: "aws_sdk_connectcases.types.template_name.TemplateName"
    """<p>A name for the template. It must be unique per domain.</p>"""
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
    status: NotRequired["aws_sdk_connectcases.types.template_status.TemplateStatus"]
    """<p>The status of the template.</p>"""
    rules: NotRequired[
        "aws_sdk_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
    ]
    r"""<p>A list of case rules (also known as <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">case field conditions</a>) on a template. </p>"""
    tag_propagation_configurations: NotRequired[
        "aws_sdk_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
    ]
    """<p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
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
    if "status" in value:
        out["status"] = value["status"]
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


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTemplateRequest.name required")
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
    if "status" in data:
        out["status"] = data["status"]
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
