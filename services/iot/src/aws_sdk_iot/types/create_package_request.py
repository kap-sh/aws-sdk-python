"""Generated from Smithy shape ``com.amazonaws.iot#CreatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.resource_description
    import aws_sdk_iot.types.tag_map


class CreatePackageRequest(TypedDict):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the new software package.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.resource_description.ResourceDescription"
    ]
    """<p>A summary of the package being created. This can be used to outline the package's contents or purpose.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_map.TagMap"]
    """<p>Metadata that can be used to manage the package.</p>"""
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_map

        out["tags"] = aws_sdk_iot.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackageRequest:
    out: CreatePackageRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_iot.types.tag_map

        out["tags"] = aws_sdk_iot.types.tag_map.deserialize_json(data["tags"])
    return out
