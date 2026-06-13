"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GetControlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_controlcatalog.types.control_aliases
    import aws_sdk_controlcatalog.types.control_arn
    import aws_sdk_controlcatalog.types.control_behavior
    import aws_sdk_controlcatalog.types.control_parameters
    import aws_sdk_controlcatalog.types.control_severity
    import aws_sdk_controlcatalog.types.governed_providers
    import aws_sdk_controlcatalog.types.governed_resources
    import aws_sdk_controlcatalog.types.implementation_details
    import aws_sdk_controlcatalog.types.parameter_requirement_summary
    import aws_sdk_controlcatalog.types.region_configuration


class GetControlResponse(TypedDict):
    arn: "aws_sdk_controlcatalog.types.control_arn.ControlArn"
    """<p>The Amazon Resource Name (ARN) of the control.</p>"""
    aliases: NotRequired["aws_sdk_controlcatalog.types.control_aliases.ControlAliases"]
    """<p>A list of alternative identifiers for the control. These are human-readable designators, such as <code>SH.S3.1</code>. Several aliases can refer to the same control across different Amazon Web Services services or compliance frameworks.</p>"""
    name: "str"
    """<p>The display name of the control.</p>"""
    description: "str"
    """<p>A description of what the control does.</p>"""
    behavior: "aws_sdk_controlcatalog.types.control_behavior.ControlBehavior"
    """<p>A term that identifies the control's functional behavior. One of <code>Preventive</code>, <code>Detective</code>, <code>Proactive</code> </p>"""
    severity: NotRequired[
        "aws_sdk_controlcatalog.types.control_severity.ControlSeverity"
    ]
    """<p>An enumerated type, with the following possible values:</p>"""
    region_configuration: (
        "aws_sdk_controlcatalog.types.region_configuration.RegionConfiguration"
    )
    implementation: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_details.ImplementationDetails"
    ]
    """<p>Returns information about the control, as an <code>ImplementationDetails</code> object that shows the underlying implementation type for a control.</p>"""
    parameter_requirement_summary: NotRequired[
        "aws_sdk_controlcatalog.types.parameter_requirement_summary.ParameterRequirementSummary"
    ]
    """<p>A summary that indicates whether the control requires parameters, accepts optional parameters, or does not support parameters. Use this field to determine whether you need to supply parameter values when you enable the control.</p>"""
    parameters: NotRequired[
        "aws_sdk_controlcatalog.types.control_parameters.ControlParameters"
    ]
    """<p>Returns an array of <code>ControlParameter</code> objects that specify the parameters a control supports. An empty list is returned for controls that don’t support parameters. </p>"""
    create_time: NotRequired["datetime.datetime"]
    """<p>A timestamp that notes the time when the control was released (start of its life) as a governance capability in Amazon Web Services.</p>"""
    governed_resources: NotRequired[
        "aws_sdk_controlcatalog.types.governed_resources.GovernedResources"
    ]
    """<p>A list of resource types that are governed by this control. This information helps you understand which controls can govern certain types of resources, and conversely, which resources are affected when the control is implemented. For Amazon Web Services controls, the resources are represented as CloudFormation resource types. For non-Amazon Web Services controls, the resources are represented in a provider-specific format. If <code>GovernedResources</code> cannot be represented by available resource types, it’s returned as an empty list.</p>"""
    governed_providers: NotRequired[
        "aws_sdk_controlcatalog.types.governed_providers.GovernedProviders"
    ]
    """<p>A list of providers whose resources are governed by this control. For example, a value of <code>AWS</code> indicates that the control governs Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetControlResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "aliases" in value:
        import aws_sdk_controlcatalog.types.control_aliases

        out["Aliases"] = aws_sdk_controlcatalog.types.control_aliases.serialize_json(
            value["aliases"]
        )
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import aws_sdk_controlcatalog.types.control_behavior

    out["Behavior"] = aws_sdk_controlcatalog.types.control_behavior.serialize_json(
        value["behavior"]
    )
    if "severity" in value:
        import aws_sdk_controlcatalog.types.control_severity

        out["Severity"] = aws_sdk_controlcatalog.types.control_severity.serialize_json(
            value["severity"]
        )
    import aws_sdk_controlcatalog.types.region_configuration

    out["RegionConfiguration"] = (
        aws_sdk_controlcatalog.types.region_configuration.serialize_json(
            value["region_configuration"]
        )
    )
    if "implementation" in value:
        import aws_sdk_controlcatalog.types.implementation_details

        out["Implementation"] = (
            aws_sdk_controlcatalog.types.implementation_details.serialize_json(
                value["implementation"]
            )
        )
    if "parameter_requirement_summary" in value:
        import aws_sdk_controlcatalog.types.parameter_requirement_summary

        out["ParameterRequirementSummary"] = (
            aws_sdk_controlcatalog.types.parameter_requirement_summary.serialize_json(
                value["parameter_requirement_summary"]
            )
        )
    if "parameters" in value:
        import aws_sdk_controlcatalog.types.control_parameters

        out["Parameters"] = (
            aws_sdk_controlcatalog.types.control_parameters.serialize_json(
                value["parameters"]
            )
        )
    if "create_time" in value:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["CreateTime"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.serialize_json(
                value["create_time"]
            )
        )
    if "governed_resources" in value:
        import aws_sdk_controlcatalog.types.governed_resources

        out["GovernedResources"] = (
            aws_sdk_controlcatalog.types.governed_resources.serialize_json(
                value["governed_resources"]
            )
        )
    if "governed_providers" in value:
        import aws_sdk_controlcatalog.types.governed_providers

        out["GovernedProviders"] = (
            aws_sdk_controlcatalog.types.governed_providers.serialize_json(
                value["governed_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetControlResponse:
    out: GetControlResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetControlResponse.arn required")
    if "Aliases" in data:
        import aws_sdk_controlcatalog.types.control_aliases

        out["aliases"] = aws_sdk_controlcatalog.types.control_aliases.deserialize_json(
            data["Aliases"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetControlResponse.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("GetControlResponse.description required")
    if "Behavior" in data:
        import aws_sdk_controlcatalog.types.control_behavior

        out["behavior"] = (
            aws_sdk_controlcatalog.types.control_behavior.deserialize_json(
                data["Behavior"]
            )
        )
    else:
        raise DeserializationError("GetControlResponse.behavior required")
    if "Severity" in data:
        import aws_sdk_controlcatalog.types.control_severity

        out["severity"] = (
            aws_sdk_controlcatalog.types.control_severity.deserialize_json(
                data["Severity"]
            )
        )
    if "RegionConfiguration" in data:
        import aws_sdk_controlcatalog.types.region_configuration

        out["region_configuration"] = (
            aws_sdk_controlcatalog.types.region_configuration.deserialize_json(
                data["RegionConfiguration"]
            )
        )
    else:
        raise DeserializationError("GetControlResponse.region_configuration required")
    if "Implementation" in data:
        import aws_sdk_controlcatalog.types.implementation_details

        out["implementation"] = (
            aws_sdk_controlcatalog.types.implementation_details.deserialize_json(
                data["Implementation"]
            )
        )
    if "ParameterRequirementSummary" in data:
        import aws_sdk_controlcatalog.types.parameter_requirement_summary

        out["parameter_requirement_summary"] = (
            aws_sdk_controlcatalog.types.parameter_requirement_summary.deserialize_json(
                data["ParameterRequirementSummary"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_controlcatalog.types.control_parameters

        out["parameters"] = (
            aws_sdk_controlcatalog.types.control_parameters.deserialize_json(
                data["Parameters"]
            )
        )
    if "CreateTime" in data:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    if "GovernedResources" in data:
        import aws_sdk_controlcatalog.types.governed_resources

        out["governed_resources"] = (
            aws_sdk_controlcatalog.types.governed_resources.deserialize_json(
                data["GovernedResources"]
            )
        )
    if "GovernedProviders" in data:
        import aws_sdk_controlcatalog.types.governed_providers

        out["governed_providers"] = (
            aws_sdk_controlcatalog.types.governed_providers.deserialize_json(
                data["GovernedProviders"]
            )
        )
    return out
