"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.user_stack_association
    import aws_sdk_appstream.types.user_stack_association_error_code


class UserStackAssociationError(TypedDict, closed=True):
    user_stack_association: NotRequired[
        "aws_sdk_appstream.types.user_stack_association.UserStackAssociation"
    ]
    """<p>Information about the user and associated stack.</p>"""
    error_code: NotRequired[
        "aws_sdk_appstream.types.user_stack_association_error_code.UserStackAssociationErrorCode"
    ]
    """<p>The error code for the error that is returned when a user can’t be associated with or disassociated from a stack.</p>"""
    error_message: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The error message for the error that is returned when a user can’t be associated with or disassociated from a stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationError) -> dict:
    out: dict = {}
    if "user_stack_association" in value:
        import aws_sdk_appstream.types.user_stack_association

        out["UserStackAssociation"] = (
            aws_sdk_appstream.types.user_stack_association.serialize_aws_json_1_1(
                value["user_stack_association"]
            )
        )
    if "error_code" in value:
        import aws_sdk_appstream.types.user_stack_association_error_code

        out["ErrorCode"] = (
            aws_sdk_appstream.types.user_stack_association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserStackAssociationError:
    out: UserStackAssociationError = {}  # type: ignore[typeddict-item]
    if "UserStackAssociation" in data:
        import aws_sdk_appstream.types.user_stack_association

        out["user_stack_association"] = (
            aws_sdk_appstream.types.user_stack_association.deserialize_aws_json_1_1(
                data["UserStackAssociation"]
            )
        )
    if "ErrorCode" in data:
        import aws_sdk_appstream.types.user_stack_association_error_code

        out["error_code"] = (
            aws_sdk_appstream.types.user_stack_association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
