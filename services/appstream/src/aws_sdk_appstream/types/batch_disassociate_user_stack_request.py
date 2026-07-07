"""Generated from Smithy shape ``com.amazonaws.appstream#BatchDisassociateUserStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.user_stack_association_list


class BatchDisassociateUserStackRequest(TypedDict, closed=True):
    user_stack_associations: NotRequired[
        "aws_sdk_appstream.types.user_stack_association_list.UserStackAssociationList"
    ]
    """<p>The list of UserStackAssociation objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDisassociateUserStackRequest) -> dict:
    out: dict = {}
    if "user_stack_associations" in value:
        import aws_sdk_appstream.types.user_stack_association_list

        out["UserStackAssociations"] = (
            aws_sdk_appstream.types.user_stack_association_list.serialize_aws_json_1_1(
                value["user_stack_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDisassociateUserStackRequest:
    out: BatchDisassociateUserStackRequest = {}  # type: ignore[typeddict-item]
    if "UserStackAssociations" in data:
        import aws_sdk_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            aws_sdk_appstream.types.user_stack_association_list.deserialize_aws_json_1_1(
                data["UserStackAssociations"]
            )
        )
    return out
