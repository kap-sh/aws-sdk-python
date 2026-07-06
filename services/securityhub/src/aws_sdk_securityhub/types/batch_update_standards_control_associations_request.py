"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateStandardsControlAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control_association_updates


class BatchUpdateStandardsControlAssociationsRequest(TypedDict, closed=True):
    standards_control_association_updates: NotRequired[
        "aws_sdk_securityhub.types.standards_control_association_updates.StandardsControlAssociationUpdates"
    ]
    """<p> Updates the enablement status of a security control in a specified standard. </p> <p> Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the control has <code>StandardsControlsUpdatable</code> value <code>NOT_READY_FOR_UPDATES</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateStandardsControlAssociationsRequest) -> dict:
    out: dict = {}
    if "standards_control_association_updates" in value:
        import aws_sdk_securityhub.types.standards_control_association_updates

        out["StandardsControlAssociationUpdates"] = (
            aws_sdk_securityhub.types.standards_control_association_updates.serialize_json(
                value["standards_control_association_updates"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateStandardsControlAssociationsRequest:
    out: BatchUpdateStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "StandardsControlAssociationUpdates" in data:
        import aws_sdk_securityhub.types.standards_control_association_updates

        out["standards_control_association_updates"] = (
            aws_sdk_securityhub.types.standards_control_association_updates.deserialize_json(
                data["StandardsControlAssociationUpdates"]
            )
        )
    return out
