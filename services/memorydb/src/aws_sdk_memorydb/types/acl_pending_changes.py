"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLPendingChanges``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user_name_list


class ACLPendingChanges(TypedDict):
    user_names_to_remove: NotRequired[
        "aws_sdk_memorydb.types.user_name_list.UserNameList"
    ]
    """<p>A list of user names being removed from the ACL</p>"""
    user_names_to_add: NotRequired["aws_sdk_memorydb.types.user_name_list.UserNameList"]
    """<p>A list of users being added to the ACL</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLPendingChanges) -> dict:
    out: dict = {}
    if "user_names_to_remove" in value:
        import aws_sdk_memorydb.types.user_name_list

        out["UserNamesToRemove"] = (
            aws_sdk_memorydb.types.user_name_list.serialize_aws_json_1_1(
                value["user_names_to_remove"]
            )
        )
    if "user_names_to_add" in value:
        import aws_sdk_memorydb.types.user_name_list

        out["UserNamesToAdd"] = (
            aws_sdk_memorydb.types.user_name_list.serialize_aws_json_1_1(
                value["user_names_to_add"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ACLPendingChanges:
    out: ACLPendingChanges = {}  # type: ignore[typeddict-item]
    if "UserNamesToRemove" in data:
        import aws_sdk_memorydb.types.user_name_list

        out["user_names_to_remove"] = (
            aws_sdk_memorydb.types.user_name_list.deserialize_aws_json_1_1(
                data["UserNamesToRemove"]
            )
        )
    if "UserNamesToAdd" in data:
        import aws_sdk_memorydb.types.user_name_list

        out["user_names_to_add"] = (
            aws_sdk_memorydb.types.user_name_list.deserialize_aws_json_1_1(
                data["UserNamesToAdd"]
            )
        )
    return out
