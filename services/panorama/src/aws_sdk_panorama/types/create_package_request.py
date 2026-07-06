"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.tag_map


class CreatePackageRequest(TypedDict, closed=True):
    package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>A name for the package.</p>"""
    tags: NotRequired["aws_sdk_panorama.types.tag_map.TagMap"]
    """<p>Tags for the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    if "tags" in value:
        import aws_sdk_panorama.types.tag_map

        out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackageRequest:
    out: CreatePackageRequest = {}  # type: ignore[typeddict-item]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("CreatePackageRequest.package_name required")
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    return out
