"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.customizable_properties
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.parameter_definitions
    import aws_sdk_securityhub.types.region_availability_status
    import aws_sdk_securityhub.types.severity_rating


class SecurityControlDefinition(TypedDict):
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number (for example, APIGateway.3). This parameter differs from <code>SecurityControlArn</code>, which is a unique Amazon Resource Name (ARN) assigned to a control. The ARN references the security control ID (for example, arn:aws:securityhub:eu-central-1:123456789012:security-control/APIGateway.3). </p>"""
    title: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The title of a security control. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of a security control across standards. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter doesn't reference a specific standard. </p>"""
    remediation_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A link to Security Hub CSPM documentation that explains how to remediate a failed finding for a security control. </p>"""
    severity_rating: NotRequired[
        "aws_sdk_securityhub.types.severity_rating.SeverityRating"
    ]
    """<p> The severity of a security control. For more information about how Security Hub CSPM determines control severity, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity\">Assigning severity to control findings</a> in the <i>Security Hub CSPM User Guide</i>. </p>"""
    current_region_availability: NotRequired[
        "aws_sdk_securityhub.types.region_availability_status.RegionAvailabilityStatus"
    ]
    """<p> Specifies whether a security control is available in the current Amazon Web Services Region. </p>"""
    customizable_properties: NotRequired[
        "aws_sdk_securityhub.types.customizable_properties.CustomizableProperties"
    ]
    """<p> Security control properties that you can customize. Currently, only parameter customization is supported for select controls. An empty array is returned for controls that don’t support custom properties. </p>"""
    parameter_definitions: NotRequired[
        "aws_sdk_securityhub.types.parameter_definitions.ParameterDefinitions"
    ]
    """<p> An object that provides a security control parameter name, description, and the options for customizing it. This object is excluded for a control that doesn't support custom parameters. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlDefinition) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "remediation_url" in value:
        out["RemediationUrl"] = value["remediation_url"]
    if "severity_rating" in value:
        import aws_sdk_securityhub.types.severity_rating

        out["SeverityRating"] = (
            aws_sdk_securityhub.types.severity_rating.serialize_json(
                value["severity_rating"]
            )
        )
    if "current_region_availability" in value:
        import aws_sdk_securityhub.types.region_availability_status

        out["CurrentRegionAvailability"] = (
            aws_sdk_securityhub.types.region_availability_status.serialize_json(
                value["current_region_availability"]
            )
        )
    if "customizable_properties" in value:
        import aws_sdk_securityhub.types.customizable_properties

        out["CustomizableProperties"] = (
            aws_sdk_securityhub.types.customizable_properties.serialize_json(
                value["customizable_properties"]
            )
        )
    if "parameter_definitions" in value:
        import aws_sdk_securityhub.types.parameter_definitions

        out["ParameterDefinitions"] = (
            aws_sdk_securityhub.types.parameter_definitions.serialize_json(
                value["parameter_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityControlDefinition:
    out: SecurityControlDefinition = {}  # type: ignore[typeddict-item]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RemediationUrl" in data:
        out["remediation_url"] = data["RemediationUrl"]
    if "SeverityRating" in data:
        import aws_sdk_securityhub.types.severity_rating

        out["severity_rating"] = (
            aws_sdk_securityhub.types.severity_rating.deserialize_json(
                data["SeverityRating"]
            )
        )
    if "CurrentRegionAvailability" in data:
        import aws_sdk_securityhub.types.region_availability_status

        out["current_region_availability"] = (
            aws_sdk_securityhub.types.region_availability_status.deserialize_json(
                data["CurrentRegionAvailability"]
            )
        )
    if "CustomizableProperties" in data:
        import aws_sdk_securityhub.types.customizable_properties

        out["customizable_properties"] = (
            aws_sdk_securityhub.types.customizable_properties.deserialize_json(
                data["CustomizableProperties"]
            )
        )
    if "ParameterDefinitions" in data:
        import aws_sdk_securityhub.types.parameter_definitions

        out["parameter_definitions"] = (
            aws_sdk_securityhub.types.parameter_definitions.deserialize_json(
                data["ParameterDefinitions"]
            )
        )
    return out
