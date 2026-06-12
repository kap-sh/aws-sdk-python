"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.user_stack_association

UserStackAssociationList: TypeAlias = list[
    "aws_sdk_appstream.types.user_stack_association.UserStackAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationList) -> list:
    import aws_sdk_appstream.types.user_stack_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.user_stack_association.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserStackAssociationList:
    import aws_sdk_appstream.types.user_stack_association

    out: UserStackAssociationList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.user_stack_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
