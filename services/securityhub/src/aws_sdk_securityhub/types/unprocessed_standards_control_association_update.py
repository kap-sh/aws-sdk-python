"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedStandardsControlAssociationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.standards_control_association_update
    import aws_sdk_securityhub.types.unprocessed_error_code


class UnprocessedStandardsControlAssociationUpdate(TypedDict):
    standards_control_association_update: NotRequired[
        "aws_sdk_securityhub.types.standards_control_association_update.StandardsControlAssociationUpdate"
    ]
    r"""<p>An array of control and standard associations for which an update failed when calling <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html\">BatchUpdateStandardsControlAssociations</a>. </p>"""
    error_code: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_error_code.UnprocessedErrorCode"
    ]
    """<p>The error code for the unprocessed update of the control's enablement status in the specified standard. The <code>NOT_FOUND</code> value has been deprecated and replaced by the <code>RESOURCE_NOT_FOUND</code> value.</p>"""
    error_reason: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason why a control's enablement status in the specified standard couldn't be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStandardsControlAssociationUpdate) -> dict:
    out: dict = {}
    if "standards_control_association_update" in value:
        import aws_sdk_securityhub.types.standards_control_association_update

        out["StandardsControlAssociationUpdate"] = (
            aws_sdk_securityhub.types.standards_control_association_update.serialize_json(
                value["standards_control_association_update"]
            )
        )
    if "error_code" in value:
        import aws_sdk_securityhub.types.unprocessed_error_code

        out["ErrorCode"] = (
            aws_sdk_securityhub.types.unprocessed_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_reason" in value:
        out["ErrorReason"] = value["error_reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedStandardsControlAssociationUpdate:
    out: UnprocessedStandardsControlAssociationUpdate = {}  # type: ignore[typeddict-item]
    if "StandardsControlAssociationUpdate" in data:
        import aws_sdk_securityhub.types.standards_control_association_update

        out["standards_control_association_update"] = (
            aws_sdk_securityhub.types.standards_control_association_update.deserialize_json(
                data["StandardsControlAssociationUpdate"]
            )
        )
    if "ErrorCode" in data:
        import aws_sdk_securityhub.types.unprocessed_error_code

        out["error_code"] = (
            aws_sdk_securityhub.types.unprocessed_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "ErrorReason" in data:
        out["error_reason"] = data["ErrorReason"]
    return out
