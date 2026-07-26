"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetStandardsControlAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control_association_ids


class BatchGetStandardsControlAssociationsRequest(TypedDict, closed=True):
    standards_control_association_ids: NotRequired[
        "capo_securityhub.types.standards_control_association_ids.StandardsControlAssociationIds"
    ]
    """<p> An array with one or more objects that includes a security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This field is used to query the enablement status of a control in a specified standard. The security control ID or ARN is the same across standards. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStandardsControlAssociationsRequest) -> dict:
    out: dict = {}
    if "standards_control_association_ids" in value:
        import capo_securityhub.types.standards_control_association_ids

        out["StandardsControlAssociationIds"] = (
            capo_securityhub.types.standards_control_association_ids.serialize_json(
                value["standards_control_association_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetStandardsControlAssociationsRequest:
    out: BatchGetStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "StandardsControlAssociationIds" in data:
        import capo_securityhub.types.standards_control_association_ids

        out["standards_control_association_ids"] = (
            capo_securityhub.types.standards_control_association_ids.deserialize_json(
                data["StandardsControlAssociationIds"]
            )
        )
    return out
