"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_status
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.related_requirements_list
    import aws_sdk_securityhub.types.timestamp


class StandardsControlAssociationSummary(TypedDict, closed=True):
    standards_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of a standard. </p>"""
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A unique standard-agnostic identifier for a control. Values for this field typically consist of an Amazon Web Services service and a number, such as APIGateway.5. This field doesn't reference a specific standard. </p>"""
    security_control_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of a control, such as <code>arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1</code>. This parameter doesn't mention a specific standard. </p>"""
    association_status: NotRequired[
        "aws_sdk_securityhub.types.association_status.AssociationStatus"
    ]
    """<p> The enablement status of a control in a specific standard. </p>"""
    related_requirements: NotRequired[
        "aws_sdk_securityhub.types.related_requirements_list.RelatedRequirementsList"
    ]
    """<p> The requirement that underlies this control in the compliance framework related to the standard. </p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The last time that a control's enablement status in a specified standard was updated.</p>"""
    updated_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason for updating a control's enablement status in a specified standard.</p>"""
    standards_control_title: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The title of a control. </p>"""
    standards_control_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of a control. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. The parameter may reference a specific standard. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationSummary) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "security_control_arn" in value:
        out["SecurityControlArn"] = value["security_control_arn"]
    if "association_status" in value:
        import aws_sdk_securityhub.types.association_status

        out["AssociationStatus"] = (
            aws_sdk_securityhub.types.association_status.serialize_json(
                value["association_status"]
            )
        )
    if "related_requirements" in value:
        import aws_sdk_securityhub.types.related_requirements_list

        out["RelatedRequirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.serialize_json(
                value["related_requirements"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_reason" in value:
        out["UpdatedReason"] = value["updated_reason"]
    if "standards_control_title" in value:
        out["StandardsControlTitle"] = value["standards_control_title"]
    if "standards_control_description" in value:
        out["StandardsControlDescription"] = value["standards_control_description"]
    return out


def deserialize_json(data: dict) -> StandardsControlAssociationSummary:
    out: StandardsControlAssociationSummary = {}  # type: ignore[typeddict-item]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "SecurityControlArn" in data:
        out["security_control_arn"] = data["SecurityControlArn"]
    if "AssociationStatus" in data:
        import aws_sdk_securityhub.types.association_status

        out["association_status"] = (
            aws_sdk_securityhub.types.association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    if "RelatedRequirements" in data:
        import aws_sdk_securityhub.types.related_requirements_list

        out["related_requirements"] = (
            aws_sdk_securityhub.types.related_requirements_list.deserialize_json(
                data["RelatedRequirements"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "UpdatedReason" in data:
        out["updated_reason"] = data["UpdatedReason"]
    if "StandardsControlTitle" in data:
        out["standards_control_title"] = data["StandardsControlTitle"]
    if "StandardsControlDescription" in data:
        out["standards_control_description"] = data["StandardsControlDescription"]
    return out
