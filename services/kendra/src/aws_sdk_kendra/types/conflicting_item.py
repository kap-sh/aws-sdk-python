"""Generated from Smithy shape ``com.amazonaws.kendra#ConflictingItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.query_text
    import aws_sdk_kendra.types.string


class ConflictingItem(TypedDict, closed=True):
    query_text: NotRequired["aws_sdk_kendra.types.query_text.QueryText"]
    """<p>The text of the conflicting query.</p>"""
    set_name: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>The name for the set of featured results that the conflicting query belongs to.</p>"""
    set_id: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>The identifier of the set of featured results that the conflicting query belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictingItem) -> dict:
    out: dict = {}
    if "query_text" in value:
        out["QueryText"] = value["query_text"]
    if "set_name" in value:
        out["SetName"] = value["set_name"]
    if "set_id" in value:
        out["SetId"] = value["set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictingItem:
    out: ConflictingItem = {}  # type: ignore[typeddict-item]
    if "QueryText" in data:
        out["query_text"] = data["QueryText"]
    if "SetName" in data:
        out["set_name"] = data["SetName"]
    if "SetId" in data:
        out["set_id"] = data["SetId"]
    return out
