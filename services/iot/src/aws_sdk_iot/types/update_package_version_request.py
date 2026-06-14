"""Generated from Smithy shape ``com.amazonaws.iot#UpdatePackageVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.package_version_action
    import aws_sdk_iot.types.package_version_artifact
    import aws_sdk_iot.types.package_version_recipe
    import aws_sdk_iot.types.resource_attributes
    import aws_sdk_iot.types.resource_description
    import aws_sdk_iot.types.version_name


class UpdatePackageVersionRequest(TypedDict):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the associated software package.</p>"""
    version_name: "aws_sdk_iot.types.version_name.VersionName"
    """<p>The name of the target package version.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.resource_description.ResourceDescription"
    ]
    """<p>The package version description.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.resource_attributes.ResourceAttributes"]
    """<p>Metadata that can be used to define a package version’s configuration. For example, the Amazon S3 file location, configuration options that are being sent to the device or fleet. </p> <p> <b>Note:</b> Attributes can be updated only when the package version is in a draft state.</p> <p>The combined size of all the attributes on a package version is limited to 3KB.</p>"""
    artifact: NotRequired[
        "aws_sdk_iot.types.package_version_artifact.PackageVersionArtifact"
    ]
    """<p>The various components that make up a software package version.</p>"""
    action: NotRequired["aws_sdk_iot.types.package_version_action.PackageVersionAction"]
    r"""<p>The status that the package version should be assigned. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle\">Package version lifecycle</a>.</p>"""
    recipe: NotRequired["aws_sdk_iot.types.package_version_recipe.PackageVersionRecipe"]
    """<p>The inline job document associated with a software package version used for a quick job deployment.</p>"""
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageVersionRequest) -> dict:
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
    if "action" in value:
        import aws_sdk_iot.types.package_version_action

        out["action"] = aws_sdk_iot.types.package_version_action.serialize_json(
            value["action"]
        )
    if "recipe" in value:
        out["recipe"] = value["recipe"]
    return out


def deserialize_json(data: dict) -> UpdatePackageVersionRequest:
    out: UpdatePackageVersionRequest = {}  # type: ignore[typeddict-item]
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
    if "action" in data:
        import aws_sdk_iot.types.package_version_action

        out["action"] = aws_sdk_iot.types.package_version_action.deserialize_json(
            data["action"]
        )
    if "recipe" in data:
        out["recipe"] = data["recipe"]
    return out
