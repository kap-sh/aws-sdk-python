"""Generated from Smithy shape ``com.amazonaws.emr#PersistentAppUI``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.persistent_app_ui_type_list
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class PersistentAppUI(TypedDict):
    persistent_app_ui_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier for the persistent application user interface object.</p>"""
    persistent_app_ui_type_list: NotRequired[
        "aws_sdk_emr.types.persistent_app_ui_type_list.PersistentAppUITypeList"
    ]
    """<p>The type list for the persistent application user interface object. Valid values include SHS, YTS, or TEZ.</p>"""
    persistent_app_ui_status: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The status for the persistent application user interface object.</p>"""
    author_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The author ID for the persistent application user interface object.</p>"""
    creation_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The creation date and time for the persistent application user interface object.</p>"""
    last_modified_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time the persistent application user interface object was last changed.</p>"""
    last_state_change_reason: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The reason the persistent application user interface object was last changed.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>A collection of tags for the persistent application user interface object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersistentAppUI) -> dict:
    out: dict = {}
    if "persistent_app_ui_id" in value:
        out["PersistentAppUIId"] = value["persistent_app_ui_id"]
    if "persistent_app_ui_type_list" in value:
        import aws_sdk_emr.types.persistent_app_ui_type_list

        out["PersistentAppUITypeList"] = (
            aws_sdk_emr.types.persistent_app_ui_type_list.serialize_aws_json_1_1(
                value["persistent_app_ui_type_list"]
            )
        )
    if "persistent_app_ui_status" in value:
        out["PersistentAppUIStatus"] = value["persistent_app_ui_status"]
    if "author_id" in value:
        out["AuthorId"] = value["author_id"]
    if "creation_time" in value:
        import aws_sdk_emr.types.date

        out["CreationTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_emr.types.date

        out["LastModifiedTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PersistentAppUI:
    out: PersistentAppUI = {}  # type: ignore[typeddict-item]
    if "PersistentAppUIId" in data:
        out["persistent_app_ui_id"] = data["PersistentAppUIId"]
    if "PersistentAppUITypeList" in data:
        import aws_sdk_emr.types.persistent_app_ui_type_list

        out["persistent_app_ui_type_list"] = (
            aws_sdk_emr.types.persistent_app_ui_type_list.deserialize_aws_json_1_1(
                data["PersistentAppUITypeList"]
            )
        )
    if "PersistentAppUIStatus" in data:
        out["persistent_app_ui_status"] = data["PersistentAppUIStatus"]
    if "AuthorId" in data:
        out["author_id"] = data["AuthorId"]
    if "CreationTime" in data:
        import aws_sdk_emr.types.date

        out["creation_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_emr.types.date

        out["last_modified_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    if "LastStateChangeReason" in data:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
