"""Generated from Smithy shape ``com.amazonaws.synthetics#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group_arn
    import capo_synthetics.types.group_name
    import capo_synthetics.types.string
    import capo_synthetics.types.tag_map
    import capo_synthetics.types.timestamp


class Group(TypedDict, closed=True):
    id: NotRequired["capo_synthetics.types.string.String"]
    """<p>The unique ID of the group.</p>"""
    name: NotRequired["capo_synthetics.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    arn: NotRequired["capo_synthetics.types.group_arn.GroupArn"]
    """<p>The ARN of the group.</p>"""
    tags: NotRequired["capo_synthetics.types.tag_map.TagMap"]
    """<p>The list of key-value pairs that are associated with the canary.</p>"""
    created_time: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time that the group was created.</p>"""
    last_modified_time: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time that the group was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "tags" in value:
        import capo_synthetics.types.tag_map

        out["Tags"] = capo_synthetics.types.tag_map.serialize_json(value["tags"])
    if "created_time" in value:
        import capo_synthetics.types.timestamp

        out["CreatedTime"] = capo_synthetics.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_synthetics.types.timestamp

        out["LastModifiedTime"] = capo_synthetics.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Tags" in data:
        import capo_synthetics.types.tag_map

        out["tags"] = capo_synthetics.types.tag_map.deserialize_json(data["Tags"])
    if "CreatedTime" in data:
        import capo_synthetics.types.timestamp

        out["created_time"] = capo_synthetics.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import capo_synthetics.types.timestamp

        out["last_modified_time"] = capo_synthetics.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
