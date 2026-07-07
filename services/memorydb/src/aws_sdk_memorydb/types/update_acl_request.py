"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.user_name_list_input


class UpdateACLRequest(TypedDict, closed=True):
    acl_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the Access Control List.</p>"""
    user_names_to_add: NotRequired[
        "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users to add to the Access Control List.</p>"""
    user_names_to_remove: NotRequired[
        "aws_sdk_memorydb.types.user_name_list_input.UserNameListInput"
    ]
    """<p>The list of users to remove from the Access Control List.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    if "user_names_to_add" in value:
        import aws_sdk_memorydb.types.user_name_list_input

        out["UserNamesToAdd"] = (
            aws_sdk_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names_to_add"]
            )
        )
    if "user_names_to_remove" in value:
        import aws_sdk_memorydb.types.user_name_list_input

        out["UserNamesToRemove"] = (
            aws_sdk_memorydb.types.user_name_list_input.serialize_aws_json_1_1(
                value["user_names_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateACLRequest:
    out: UpdateACLRequest = {}  # type: ignore[typeddict-item]
    if "ACLName" in data:
        out["acl_name"] = data["ACLName"]
    else:
        raise DeserializationError("UpdateACLRequest.acl_name required")
    if "UserNamesToAdd" in data:
        import aws_sdk_memorydb.types.user_name_list_input

        out["user_names_to_add"] = (
            aws_sdk_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNamesToAdd"]
            )
        )
    if "UserNamesToRemove" in data:
        import aws_sdk_memorydb.types.user_name_list_input

        out["user_names_to_remove"] = (
            aws_sdk_memorydb.types.user_name_list_input.deserialize_aws_json_1_1(
                data["UserNamesToRemove"]
            )
        )
    return out
