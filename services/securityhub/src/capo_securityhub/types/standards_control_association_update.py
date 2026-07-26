"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.association_status
    import capo_securityhub.types.non_empty_string


class StandardsControlAssociationUpdate(TypedDict, closed=True):
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the standard in which you want to update the control's enablement status.</p>"""
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The unique identifier for the security control whose enablement status you want to update.</p>"""
    association_status: NotRequired[
        "capo_securityhub.types.association_status.AssociationStatus"
    ]
    """<p>The desired enablement status of the control in the standard.</p>"""
    updated_reason: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason for updating the control's enablement status in the standard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationUpdate) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "association_status" in value:
        import capo_securityhub.types.association_status

        out["AssociationStatus"] = (
            capo_securityhub.types.association_status.serialize_json(
                value["association_status"]
            )
        )
    if "updated_reason" in value:
        out["UpdatedReason"] = value["updated_reason"]
    return out


def deserialize_json(data: dict) -> StandardsControlAssociationUpdate:
    out: StandardsControlAssociationUpdate = {}  # type: ignore[typeddict-item]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "AssociationStatus" in data:
        import capo_securityhub.types.association_status

        out["association_status"] = (
            capo_securityhub.types.association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    if "UpdatedReason" in data:
        out["updated_reason"] = data["UpdatedReason"]
    return out
