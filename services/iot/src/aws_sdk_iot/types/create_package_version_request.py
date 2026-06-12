"""Generated from Smithy shape ``com.amazonaws.iot#CreatePackageVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.package_version_artifact
    import aws_sdk_iot.types.package_version_recipe
    import aws_sdk_iot.types.resource_attributes
    import aws_sdk_iot.types.resource_description
    import aws_sdk_iot.types.tag_map
    import aws_sdk_iot.types.version_name


class CreatePackageVersionRequest(TypedDict):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the associated software package.</p>"""
    version_name: "aws_sdk_iot.types.version_name.VersionName"
    """<p>The name of the new package version.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.resource_description.ResourceDescription"
    ]
    """<p>A summary of the package version being created. This can be used to outline the package's contents or purpose.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.resource_attributes.ResourceAttributes"]
    """<p>Metadata that can be used to define a package version’s configuration. For example, the S3 file location, configuration options that are being sent to the device or fleet.</p> <p>The combined size of all the attributes on a package version is limited to 3KB.</p>"""
    artifact: NotRequired[
        "aws_sdk_iot.types.package_version_artifact.PackageVersionArtifact"
    ]
    """<p>The various build components created during the build process such as libraries and configuration files that make up a software package version.</p>"""
    recipe: NotRequired["aws_sdk_iot.types.package_version_recipe.PackageVersionRecipe"]
    """<p>The inline job document associated with a software package version used for a quick job deployment.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_map.TagMap"]
    """<p>Metadata that can be used to manage the package version.</p>"""
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        import aws_sdk_iot.types.resource_attributes

        out["attributes"] = aws_sdk_iot.types.resource_attributes.serialize_json(
            value["attributes"]
        )
    if "artifact" in value:
        import aws_sdk_iot.types.package_version_artifact

        out["artifact"] = aws_sdk_iot.types.package_version_artifact.serialize_json(
            value["artifact"]
        )
    if "recipe" in value:
        out["recipe"] = value["recipe"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_map

        out["tags"] = aws_sdk_iot.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePackageVersionRequest:
    out: CreatePackageVersionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "attributes" in data:
        import aws_sdk_iot.types.resource_attributes

        out["attributes"] = aws_sdk_iot.types.resource_attributes.deserialize_json(
            data["attributes"]
        )
    if "artifact" in data:
        import aws_sdk_iot.types.package_version_artifact

        out["artifact"] = aws_sdk_iot.types.package_version_artifact.deserialize_json(
            data["artifact"]
        )
    if "recipe" in data:
        out["recipe"] = data["recipe"]
    if "tags" in data:
        import aws_sdk_iot.types.tag_map

        out["tags"] = aws_sdk_iot.types.tag_map.deserialize_json(data["tags"])
    return out
