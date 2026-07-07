"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_origin_configuration


class PackageDescription(TypedDict, closed=True):
    format: NotRequired["aws_sdk_codeartifact.types.package_format.PackageFormat"]
    """<p>A format that specifies the type of the package.</p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    name: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p>The name of the package.</p>"""
    origin_configuration: NotRequired[
        "aws_sdk_codeartifact.types.package_origin_configuration.PackageOriginConfiguration"
    ]
    """<p>The package origin configuration for the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageDescription) -> dict:
    out: dict = {}
    if "format" in value:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "name" in value:
        out["name"] = value["name"]
    if "origin_configuration" in value:
        import aws_sdk_codeartifact.types.package_origin_configuration

        out["originConfiguration"] = (
            aws_sdk_codeartifact.types.package_origin_configuration.serialize_json(
                value["origin_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageDescription:
    out: PackageDescription = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "name" in data:
        out["name"] = data["name"]
    if "originConfiguration" in data:
        import aws_sdk_codeartifact.types.package_origin_configuration

        out["origin_configuration"] = (
            aws_sdk_codeartifact.types.package_origin_configuration.deserialize_json(
                data["originConfiguration"]
            )
        )
    return out
