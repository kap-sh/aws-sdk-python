"""Generated from Smithy shape ``com.amazonaws.appstream#BatchAssociateUserStackResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.user_stack_association_error_list


class BatchAssociateUserStackResult(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_appstream.types.user_stack_association_error_list.UserStackAssociationErrorList"
    ]
    """<p>The list of UserStackAssociationError objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateUserStackResult) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_appstream.types.user_stack_association_error_list

        out["errors"] = (
            aws_sdk_appstream.types.user_stack_association_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateUserStackResult:
    out: BatchAssociateUserStackResult = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_appstream.types.user_stack_association_error_list

        out["errors"] = (
            aws_sdk_appstream.types.user_stack_association_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
