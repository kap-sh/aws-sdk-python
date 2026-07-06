"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateStandardsControlAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.unprocessed_standards_control_association_updates


class BatchUpdateStandardsControlAssociationsResponse(TypedDict, closed=True):
    unprocessed_association_updates: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_standards_control_association_updates.UnprocessedStandardsControlAssociationUpdates"
    ]
    """<p> A security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) whose enablement status in a specified standard couldn't be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateStandardsControlAssociationsResponse) -> dict:
    out: dict = {}
    if "unprocessed_association_updates" in value:
        import aws_sdk_securityhub.types.unprocessed_standards_control_association_updates

        out["UnprocessedAssociationUpdates"] = (
            aws_sdk_securityhub.types.unprocessed_standards_control_association_updates.serialize_json(
                value["unprocessed_association_updates"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateStandardsControlAssociationsResponse:
    out: BatchUpdateStandardsControlAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "UnprocessedAssociationUpdates" in data:
        import aws_sdk_securityhub.types.unprocessed_standards_control_association_updates

        out["unprocessed_association_updates"] = (
            aws_sdk_securityhub.types.unprocessed_standards_control_association_updates.deserialize_json(
                data["UnprocessedAssociationUpdates"]
            )
        )
    return out
