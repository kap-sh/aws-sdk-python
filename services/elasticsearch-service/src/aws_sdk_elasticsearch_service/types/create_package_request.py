"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.package_description
    import aws_sdk_elasticsearch_service.types.package_name
    import aws_sdk_elasticsearch_service.types.package_source
    import aws_sdk_elasticsearch_service.types.package_type


class CreatePackageRequest(TypedDict):
    package_name: "aws_sdk_elasticsearch_service.types.package_name.PackageName"
    """<p>Unique identifier for the package.</p>"""
    package_type: "aws_sdk_elasticsearch_service.types.package_type.PackageType"
    """<p>Type of package. Currently supports only TXT-DICTIONARY.</p>"""
    package_description: NotRequired[
        "aws_sdk_elasticsearch_service.types.package_description.PackageDescription"
    ]
    """<p>Description of the package.</p>"""
    package_source: "aws_sdk_elasticsearch_service.types.package_source.PackageSource"
    """<p>The customer S3 location <code>PackageSource</code> for importing the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    import aws_sdk_elasticsearch_service.types.package_type

    out["PackageType"] = (
        aws_sdk_elasticsearch_service.types.package_type.serialize_json(
            value["package_type"]
        )
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    import aws_sdk_elasticsearch_service.types.package_source

    out["PackageSource"] = (
        aws_sdk_elasticsearch_service.types.package_source.serialize_json(
            value["package_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePackageRequest:
    out: CreatePackageRequest = {}  # type: ignore[typeddict-item]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("CreatePackageRequest.package_name required")
    if "PackageType" in data:
        import aws_sdk_elasticsearch_service.types.package_type

        out["package_type"] = (
            aws_sdk_elasticsearch_service.types.package_type.deserialize_json(
                data["PackageType"]
            )
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_type required")
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "PackageSource" in data:
        import aws_sdk_elasticsearch_service.types.package_source

        out["package_source"] = (
            aws_sdk_elasticsearch_service.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_source required")
    return out
