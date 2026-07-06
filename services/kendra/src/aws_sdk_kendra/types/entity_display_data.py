"""Generated from Smithy shape ``com.amazonaws.kendra#EntityDisplayData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.name_type


class EntityDisplayData(TypedDict, closed=True):
    user_name: NotRequired["aws_sdk_kendra.types.name_type.NameType"]
    """<p>The name of the user.</p>"""
    group_name: NotRequired["aws_sdk_kendra.types.name_type.NameType"]
    """<p>The name of the group.</p>"""
    identified_user_name: NotRequired["aws_sdk_kendra.types.name_type.NameType"]
    """<p>The user name of the user.</p>"""
    first_name: NotRequired["aws_sdk_kendra.types.name_type.NameType"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_kendra.types.name_type.NameType"]
    """<p>The last name of the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityDisplayData) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "identified_user_name" in value:
        out["IdentifiedUserName"] = value["identified_user_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityDisplayData:
    out: EntityDisplayData = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "IdentifiedUserName" in data:
        out["identified_user_name"] = data["IdentifiedUserName"]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    return out
