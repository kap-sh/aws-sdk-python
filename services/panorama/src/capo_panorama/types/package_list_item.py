"""Generated from Smithy shape ``com.amazonaws.panorama#PackageListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_name
    import capo_panorama.types.tag_map
    import capo_panorama.types.time_stamp


class PackageListItem(TypedDict, closed=True):
    package_id: NotRequired["capo_panorama.types.node_package_id.NodePackageId"]
    """<p>The package's ID.</p>"""
    package_name: NotRequired["capo_panorama.types.node_package_name.NodePackageName"]
    """<p>The package's name.</p>"""
    arn: NotRequired["capo_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The package's ARN.</p>"""
    created_time: NotRequired["capo_panorama.types.time_stamp.TimeStamp"]
    """<p>When the package was created.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>The package's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageListItem) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageId"] = value["package_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import capo_panorama.types.time_stamp

        out["CreatedTime"] = capo_panorama.types.time_stamp.serialize_json(
            value["created_time"]
        )
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PackageListItem:
    out: PackageListItem = {}  # type: ignore[typeddict-item]
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import capo_panorama.types.time_stamp

        out["created_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Tags" in data:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    return out
