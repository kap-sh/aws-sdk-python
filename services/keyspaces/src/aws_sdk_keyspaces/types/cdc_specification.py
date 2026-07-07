"""Generated from Smithy shape ``com.amazonaws.keyspaces#CdcSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.cdc_propagate_tags
    import aws_sdk_keyspaces.types.cdc_status
    import aws_sdk_keyspaces.types.tag_list
    import aws_sdk_keyspaces.types.view_type


class CdcSpecification(TypedDict, closed=True):
    status: "aws_sdk_keyspaces.types.cdc_status.CdcStatus"
    """<p>The status of the CDC stream. You can enable or disable a stream for a table.</p>"""
    view_type: NotRequired["aws_sdk_keyspaces.types.view_type.ViewType"]
    """<p>The view type specifies the changes Amazon Keyspaces records for each changed row in the stream. After you create the stream, you can't make changes to this selection. </p> <p>The options are:</p> <ul> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - both versions of the row, before and after the change. This is the default.</p> </li> <li> <p> <code>NEW_IMAGE</code> - the version of the row after the change.</p> </li> <li> <p> <code>OLD_IMAGE</code> - the version of the row before the change.</p> </li> <li> <p> <code>KEYS_ONLY</code> - the partition and clustering keys of the row that was changed.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_keyspaces.types.tag_list.TagList"]
    """<p>The tags (key-value pairs) that you want to apply to the stream.</p>"""
    propagate_tags: NotRequired[
        "aws_sdk_keyspaces.types.cdc_propagate_tags.CdcPropagateTags"
    ]
    """<p>Specifies that the stream inherits the tags from the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CdcSpecification) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "view_type" in value:
        out["viewType"] = value["view_type"]
    if "tags" in value:
        import aws_sdk_keyspaces.types.tag_list

        out["tags"] = aws_sdk_keyspaces.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "propagate_tags" in value:
        out["propagateTags"] = value["propagate_tags"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CdcSpecification:
    out: CdcSpecification = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("CdcSpecification.status required")
    if "viewType" in data:
        out["view_type"] = data["viewType"]
    if "tags" in data:
        import aws_sdk_keyspaces.types.tag_list

        out["tags"] = aws_sdk_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "propagateTags" in data:
        out["propagate_tags"] = data["propagateTags"]
    return out
