"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.license_info_list
    import aws_sdk_codeartifact.types.package_format
    import aws_sdk_codeartifact.types.package_name
    import aws_sdk_codeartifact.types.package_namespace
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.package_version_origin
    import aws_sdk_codeartifact.types.package_version_revision
    import aws_sdk_codeartifact.types.package_version_status
    import aws_sdk_codeartifact.types.string
    import aws_sdk_codeartifact.types.string255
    import aws_sdk_codeartifact.types.timestamp


class PackageVersionDescription(TypedDict):
    format: NotRequired["aws_sdk_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package version. </p>"""
    namespace: NotRequired[
        "aws_sdk_codeartifact.types.package_namespace.PackageNamespace"
    ]
    """<p>The namespace of the package version. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package_name: NotRequired["aws_sdk_codeartifact.types.package_name.PackageName"]
    """<p> The name of the requested package. </p>"""
    display_name: NotRequired["aws_sdk_codeartifact.types.string255.String255"]
    """<p> The name of the package that is displayed. The <code>displayName</code> varies depending on the package version's format. For example, if an npm package is named <code>ui</code>, is in the namespace <code>vue</code>, and has the format <code>npm</code>, then the <code>displayName</code> is <code>@vue/ui</code>. </p>"""
    version: NotRequired["aws_sdk_codeartifact.types.package_version.PackageVersion"]
    """<p> The version of the package. </p>"""
    summary: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> A summary of the package version. The summary is extracted from the package. The information in and detail level of the summary depends on the package version's format. </p>"""
    home_page: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The homepage associated with the package. </p>"""
    source_code_repository: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The repository for the source code in the package version, or the source code used to build it. </p>"""
    published_time: NotRequired["aws_sdk_codeartifact.types.timestamp.Timestamp"]
    """<p> A timestamp that contains the date and time the package version was published. </p>"""
    licenses: NotRequired[
        "aws_sdk_codeartifact.types.license_info_list.LicenseInfoList"
    ]
    """<p> Information about licenses associated with the package version. </p>"""
    revision: NotRequired[
        "aws_sdk_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The revision of the package version. </p>"""
    status: NotRequired[
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> A string that contains the status of the package version. </p>"""
    origin: NotRequired[
        "aws_sdk_codeartifact.types.package_version_origin.PackageVersionOrigin"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html\">PackageVersionOrigin</a> object that contains information about how the package version was added to the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionDescription) -> dict:
    out: dict = {}
    if "format" in value:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "home_page" in value:
        out["homePage"] = value["home_page"]
    if "source_code_repository" in value:
        out["sourceCodeRepository"] = value["source_code_repository"]
    if "published_time" in value:
        import aws_sdk_codeartifact.types.timestamp

        out["publishedTime"] = aws_sdk_codeartifact.types.timestamp.serialize_json(
            value["published_time"]
        )
    if "licenses" in value:
        import aws_sdk_codeartifact.types.license_info_list

        out["licenses"] = aws_sdk_codeartifact.types.license_info_list.serialize_json(
            value["licenses"]
        )
    if "revision" in value:
        out["revision"] = value["revision"]
    if "status" in value:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.serialize_json(
                value["status"]
            )
        )
    if "origin" in value:
        import aws_sdk_codeartifact.types.package_version_origin

        out["origin"] = (
            aws_sdk_codeartifact.types.package_version_origin.serialize_json(
                value["origin"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageVersionDescription:
    out: PackageVersionDescription = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_codeartifact.types.package_format

        out["format"] = aws_sdk_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "version" in data:
        out["version"] = data["version"]
    if "summary" in data:
        out["summary"] = data["summary"]
    if "homePage" in data:
        out["home_page"] = data["homePage"]
    if "sourceCodeRepository" in data:
        out["source_code_repository"] = data["sourceCodeRepository"]
    if "publishedTime" in data:
        import aws_sdk_codeartifact.types.timestamp

        out["published_time"] = aws_sdk_codeartifact.types.timestamp.deserialize_json(
            data["publishedTime"]
        )
    if "licenses" in data:
        import aws_sdk_codeartifact.types.license_info_list

        out["licenses"] = aws_sdk_codeartifact.types.license_info_list.deserialize_json(
            data["licenses"]
        )
    if "revision" in data:
        out["revision"] = data["revision"]
    if "status" in data:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.deserialize_json(
                data["status"]
            )
        )
    if "origin" in data:
        import aws_sdk_codeartifact.types.package_version_origin

        out["origin"] = (
            aws_sdk_codeartifact.types.package_version_origin.deserialize_json(
                data["origin"]
            )
        )
    return out
