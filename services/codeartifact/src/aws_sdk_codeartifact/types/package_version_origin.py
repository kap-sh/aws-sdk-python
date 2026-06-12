"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionOrigin``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.domain_entry_point
    import aws_sdk_codeartifact.types.package_version_origin_type


class PackageVersionOrigin(TypedDict):
    domain_entry_point: NotRequired[
        "aws_sdk_codeartifact.types.domain_entry_point.DomainEntryPoint"
    ]
    """<p>A <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainEntryPoint.html\">DomainEntryPoint</a> object that contains information about from which repository or external connection the package version was added to the domain.</p>"""
    origin_type: NotRequired[
        "aws_sdk_codeartifact.types.package_version_origin_type.PackageVersionOriginType"
    ]
    """<p>Describes how the package version was originally added to the domain. An <code>INTERNAL</code> origin type means the package version was published directly to a repository in the domain. An <code>EXTERNAL</code> origin type means the package version was ingested from an external connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionOrigin) -> dict:
    out: dict = {}
    if "domain_entry_point" in value:
        import aws_sdk_codeartifact.types.domain_entry_point

        out["domainEntryPoint"] = (
            aws_sdk_codeartifact.types.domain_entry_point.serialize_json(
                value["domain_entry_point"]
            )
        )
    if "origin_type" in value:
        import aws_sdk_codeartifact.types.package_version_origin_type

        out["originType"] = (
            aws_sdk_codeartifact.types.package_version_origin_type.serialize_json(
                value["origin_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageVersionOrigin:
    out: PackageVersionOrigin = {}  # type: ignore[typeddict-item]
    if "domainEntryPoint" in data:
        import aws_sdk_codeartifact.types.domain_entry_point

        out["domain_entry_point"] = (
            aws_sdk_codeartifact.types.domain_entry_point.deserialize_json(
                data["domainEntryPoint"]
            )
        )
    if "originType" in data:
        import aws_sdk_codeartifact.types.package_version_origin_type

        out["origin_type"] = (
            aws_sdk_codeartifact.types.package_version_origin_type.deserialize_json(
                data["originType"]
            )
        )
    return out
