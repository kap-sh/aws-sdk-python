"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.control_status
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.related_requirements_list
    import aws_sdk_securityhub.types.severity_rating
    import aws_sdk_securityhub.types.timestamp


class StandardsControl(TypedDict):
    standards_control_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the security standard control.</p>"""
    control_status: NotRequired[
        "aws_sdk_securityhub.types.control_status.ControlStatus"
    ]
    """<p>The current status of the security standard control. Indicates whether the control is enabled or disabled. Security Hub CSPM does not check against disabled controls.</p>"""
    disabled_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason provided for the most recent change in status for the control.</p>"""
    control_status_updated_at: NotRequired[
        "aws_sdk_securityhub.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the status of the security standard control was most recently updated.</p>"""
    control_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the security standard control.</p>"""
    title: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The title of the security standard control.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The longer description of the security standard control. Provides information about what the control is checking for.</p>"""
    remediation_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A link to remediation information for the control in the Security Hub CSPM user documentation.</p>"""
    severity_rating: NotRequired[
        "aws_sdk_securityhub.types.severity_rating.SeverityRating"
    ]
    """<p>The severity of findings generated from this security standard control.</p> <p>The finding severity is based on an assessment of how easy it would be to compromise Amazon Web Services resources if the issue is detected.</p>"""
    related_requirements: NotRequired[
        "aws_sdk_securityhub.types.related_requirements_list.RelatedRequirementsList"
    ]
    """<p>The list of requirements that are related to this control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControl) -> dict:
    out: dict = {}
    if "standards_control_arn" in value:
        out["StandardsControlArn"] = value["standards_control_arn"]
    if "control_status" in value:
        import aws_sdk_securityhub.types.control_status

        out["ControlStatus"] = aws_sdk_securityhub.types.control_status.serialize_json(
            value["control_status"]
        )
    if "disabled_reason" in value:
        out["DisabledReason"] = value["disabled_reason"]
    if "control_status_updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["ControlStatusUpdatedAt"] = (
            aws_sdk_securityhub.types.timestamp.serialize_json(
                value["control_status_updated_at"]
            )
        )
    if "control_id" in value:
        out["ControlId"] = value["control_id"]
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
    if "related_requirements" in value:
        import aws_sdk_securityhub.types.related_requirements_list

        out["RelatedRequirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.serialize_json(
                value["related_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardsControl:
    out: StandardsControl = {}  # type: ignore[typeddict-item]
    if "StandardsControlArn" in data:
        out["standards_control_arn"] = data["StandardsControlArn"]
    if "ControlStatus" in data:
        import aws_sdk_securityhub.types.control_status

        out["control_status"] = (
            aws_sdk_securityhub.types.control_status.deserialize_json(
                data["ControlStatus"]
            )
        )
    if "DisabledReason" in data:
        out["disabled_reason"] = data["DisabledReason"]
    if "ControlStatusUpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["control_status_updated_at"] = (
            aws_sdk_securityhub.types.timestamp.deserialize_json(
                data["ControlStatusUpdatedAt"]
            )
        )
    if "ControlId" in data:
        out["control_id"] = data["ControlId"]
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
    if "RelatedRequirements" in data:
        import aws_sdk_securityhub.types.related_requirements_list

        out["related_requirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.deserialize_json(
                data["RelatedRequirements"]
            )
        )
    return out
