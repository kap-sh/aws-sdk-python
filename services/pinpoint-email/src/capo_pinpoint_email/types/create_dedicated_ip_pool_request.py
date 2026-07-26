"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateDedicatedIpPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.pool_name
    import capo_pinpoint_email.types.tag_list


class CreateDedicatedIpPoolRequest(TypedDict, closed=True):
    pool_name: "capo_pinpoint_email.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    tags: NotRequired["capo_pinpoint_email.types.tag_list.TagList"]
    """<p>An object that defines the tags (keys and values) that you want to associate with the pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDedicatedIpPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    if "tags" in value:
        import capo_pinpoint_email.types.tag_list

        out["Tags"] = capo_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDedicatedIpPoolRequest:
    out: CreateDedicatedIpPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError("CreateDedicatedIpPoolRequest.pool_name required")
    if "Tags" in data:
        import capo_pinpoint_email.types.tag_list

        out["tags"] = capo_pinpoint_email.types.tag_list.deserialize_json(data["Tags"])
    return out
