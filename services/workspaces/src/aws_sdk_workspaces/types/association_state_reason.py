"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationStateReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.association_error_code
    import aws_sdk_workspaces.types.string2048


class AssociationStateReason(TypedDict, closed=True):
    error_code: NotRequired[
        "aws_sdk_workspaces.types.association_error_code.AssociationErrorCode"
    ]
    """<p>The error code of the association deployment failure.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.string2048.String2048"]
    """<p>The error message of the association deployment failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStateReason) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_workspaces.types.association_error_code

        out["ErrorCode"] = (
            aws_sdk_workspaces.types.association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationStateReason:
    out: AssociationStateReason = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_workspaces.types.association_error_code

        out["error_code"] = (
            aws_sdk_workspaces.types.association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
