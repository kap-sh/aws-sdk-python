"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUserStackAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.user_stack_association_list


class DescribeUserStackAssociationsResult(TypedDict, closed=True):
    user_stack_associations: NotRequired[
        "aws_sdk_appstream.types.user_stack_association_list.UserStackAssociationList"
    ]
    """<p>The UserStackAssociation objects.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserStackAssociationsResult) -> dict:
    out: dict = {}
    if "user_stack_associations" in value:
        import aws_sdk_appstream.types.user_stack_association_list

        out["UserStackAssociations"] = (
            aws_sdk_appstream.types.user_stack_association_list.serialize_aws_json_1_1(
                value["user_stack_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserStackAssociationsResult:
    out: DescribeUserStackAssociationsResult = {}  # type: ignore[typeddict-item]
    if "UserStackAssociations" in data:
        import aws_sdk_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            aws_sdk_appstream.types.user_stack_association_list.deserialize_aws_json_1_1(
                data["UserStackAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
