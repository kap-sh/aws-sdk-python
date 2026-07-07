"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetStandardsControlAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control_association_details
    import aws_sdk_securityhub.types.unprocessed_standards_control_associations


class BatchGetStandardsControlAssociationsResponse(TypedDict, closed=True):
    standards_control_association_details: NotRequired[
        "aws_sdk_securityhub.types.standards_control_association_details.StandardsControlAssociationDetails"
    ]
    """<p>Provides the enablement status of a security control in a specified standard and other details for the control in relation to the specified standard. </p>"""
    unprocessed_associations: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_standards_control_associations.UnprocessedStandardsControlAssociations"
    ]
    """<p> A security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) whose enablement status in a specified standard cannot be returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStandardsControlAssociationsResponse) -> dict:
    out: dict = {}
    if "standards_control_association_details" in value:
        import aws_sdk_securityhub.types.standards_control_association_details

        out["StandardsControlAssociationDetails"] = (
            aws_sdk_securityhub.types.standards_control_association_details.serialize_json(
                value["standards_control_association_details"]
            )
        )
    if "unprocessed_associations" in value:
        import aws_sdk_securityhub.types.unprocessed_standards_control_associations

        out["UnprocessedAssociations"] = (
            aws_sdk_securityhub.types.unprocessed_standards_control_associations.serialize_json(
                value["unprocessed_associations"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetStandardsControlAssociationsResponse:
    out: BatchGetStandardsControlAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "StandardsControlAssociationDetails" in data:
        import aws_sdk_securityhub.types.standards_control_association_details

        out["standards_control_association_details"] = (
            aws_sdk_securityhub.types.standards_control_association_details.deserialize_json(
                data["StandardsControlAssociationDetails"]
            )
        )
    if "UnprocessedAssociations" in data:
        import aws_sdk_securityhub.types.unprocessed_standards_control_associations

        out["unprocessed_associations"] = (
            aws_sdk_securityhub.types.unprocessed_standards_control_associations.deserialize_json(
                data["UnprocessedAssociations"]
            )
        )
    return out
