"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositoryExternalConnectionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.external_connection_name
    import aws_sdk_codeartifact.types.external_connection_status
    import aws_sdk_codeartifact.types.package_format


class RepositoryExternalConnectionInfo(TypedDict, closed=True):
    external_connection_name: NotRequired[
        "aws_sdk_codeartifact.types.external_connection_name.ExternalConnectionName"
    ]
    """<p> The name of the external connection associated with a repository. </p>"""
    package_format: NotRequired[
        "aws_sdk_codeartifact.types.package_format.PackageFormat"
    ]
    """<p> The package format associated with a repository's external connection. The valid package formats are: </p> <ul> <li> <p> <code>npm</code>: A Node Package Manager (npm) package. </p> </li> <li> <p> <code>pypi</code>: A Python Package Index (PyPI) package. </p> </li> <li> <p> <code>maven</code>: A Maven package that contains compiled code in a distributable format, such as a JAR file. </p> </li> <li> <p> <code>nuget</code>: A NuGet package. </p> </li> <li> <p> <code>generic</code>: A generic package. </p> </li> <li> <p> <code>ruby</code>: A Ruby package. </p> </li> <li> <p> <code>swift</code>: A Swift package. </p> </li> <li> <p> <code>cargo</code>: A Cargo package. </p> </li> </ul>"""
    status: NotRequired[
        "aws_sdk_codeartifact.types.external_connection_status.ExternalConnectionStatus"
    ]
    """<p> The status of the external connection of a repository. There is one valid value, <code>Available</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryExternalConnectionInfo) -> dict:
    out: dict = {}
    if "external_connection_name" in value:
        out["externalConnectionName"] = value["external_connection_name"]
    if "package_format" in value:
        import aws_sdk_codeartifact.types.package_format

        out["packageFormat"] = aws_sdk_codeartifact.types.package_format.serialize_json(
            value["package_format"]
        )
    if "status" in value:
        import aws_sdk_codeartifact.types.external_connection_status

        out["status"] = (
            aws_sdk_codeartifact.types.external_connection_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> RepositoryExternalConnectionInfo:
    out: RepositoryExternalConnectionInfo = {}  # type: ignore[typeddict-item]
    if "externalConnectionName" in data:
        out["external_connection_name"] = data["externalConnectionName"]
    if "packageFormat" in data:
        import aws_sdk_codeartifact.types.package_format

        out["package_format"] = (
            aws_sdk_codeartifact.types.package_format.deserialize_json(
                data["packageFormat"]
            )
        )
    if "status" in data:
        import aws_sdk_codeartifact.types.external_connection_status

        out["status"] = (
            aws_sdk_codeartifact.types.external_connection_status.deserialize_json(
                data["status"]
            )
        )
    return out
