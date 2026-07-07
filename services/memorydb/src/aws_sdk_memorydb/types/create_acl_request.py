"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list
    import aws_sdk_memorydb.types.user_name_list_input


class CreateACLRequest(TypedDict, closed=True):
    acl_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the Access Control List.</p>"""
    user_names: NotRequired[
        "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users that belong to the Access Control List.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    if "user_names" in value:
        import aws_sdk_memorydb.types.user_name_list_input

        out["UserNames"] = (
            aws_sdk_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names"]
            )
        )
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateACLRequest:
    out: CreateACLRequest = {}  # type: ignore[typeddict-item]
    if "ACLName" in data:
        out["acl_name"] = data["ACLName"]
    else:
        raise DeserializationError("CreateACLRequest.acl_name required")
    if "UserNames" in data:
        import aws_sdk_memorydb.types.user_name_list_input

        out["user_names"] = (
            aws_sdk_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNames"]
            )
        )
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
