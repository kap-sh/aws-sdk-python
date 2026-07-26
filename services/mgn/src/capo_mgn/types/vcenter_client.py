"""Generated from Smithy shape ``com.amazonaws.mgn#VcenterClient``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.bounded_string
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.tags_map
    import capo_mgn.types.vcenter_client_id


class VcenterClient(TypedDict, closed=True):
    vcenter_client_id: NotRequired["capo_mgn.types.vcenter_client_id.VcenterClientID"]
    """<p>ID of vCenter client.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Arn of vCenter client.</p>"""
    hostname: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Hostname of vCenter client .</p>"""
    vcenter_uuid: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Vcenter UUID of vCenter client.</p>"""
    datacenter_name: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Datacenter name of vCenter client.</p>"""
    last_seen_datetime: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Last seen time of vCenter client.</p>"""
    source_server_tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags for Source Server of vCenter client.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags for vCenter client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VcenterClient) -> dict:
    out: dict = {}
    if "vcenter_client_id" in value:
        out["vcenterClientID"] = value["vcenter_client_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "vcenter_uuid" in value:
        out["vcenterUUID"] = value["vcenter_uuid"]
    if "datacenter_name" in value:
        out["datacenterName"] = value["datacenter_name"]
    if "last_seen_datetime" in value:
        out["lastSeenDatetime"] = value["last_seen_datetime"]
    if "source_server_tags" in value:
        import capo_mgn.types.tags_map

        out["sourceServerTags"] = capo_mgn.types.tags_map.serialize_json(
            value["source_server_tags"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> VcenterClient:
    out: VcenterClient = {}  # type: ignore[typeddict-item]
    if "vcenterClientID" in data:
        out["vcenter_client_id"] = data["vcenterClientID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "vcenterUUID" in data:
        out["vcenter_uuid"] = data["vcenterUUID"]
    if "datacenterName" in data:
        out["datacenter_name"] = data["datacenterName"]
    if "lastSeenDatetime" in data:
        out["last_seen_datetime"] = data["lastSeenDatetime"]
    if "sourceServerTags" in data:
        import capo_mgn.types.tags_map

        out["source_server_tags"] = capo_mgn.types.tags_map.deserialize_json(
            data["sourceServerTags"]
        )
    if "tags" in data:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
