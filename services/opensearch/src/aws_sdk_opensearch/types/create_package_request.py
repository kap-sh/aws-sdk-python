"""Generated from Smithy shape ``com.amazonaws.opensearch#CreatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.engine_version
    import aws_sdk_opensearch.types.package_configuration
    import aws_sdk_opensearch.types.package_description
    import aws_sdk_opensearch.types.package_encryption_options
    import aws_sdk_opensearch.types.package_name
    import aws_sdk_opensearch.types.package_source
    import aws_sdk_opensearch.types.package_type
    import aws_sdk_opensearch.types.package_vending_options


class CreatePackageRequest(TypedDict):
    package_name: "aws_sdk_opensearch.types.package_name.PackageName"
    """<p>Unique name for the package.</p>"""
    package_type: "aws_sdk_opensearch.types.package_type.PackageType"
    """<p>The type of package.</p>"""
    package_description: NotRequired[
        "aws_sdk_opensearch.types.package_description.PackageDescription"
    ]
    """<p>Description of the package.</p>"""
    package_source: "aws_sdk_opensearch.types.package_source.PackageSource"
    """<p>The Amazon S3 location from which to import the package.</p>"""
    package_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p> The configuration parameters for the package being created.</p>"""
    engine_version: NotRequired["aws_sdk_opensearch.types.engine_version.EngineVersion"]
    """<p>The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type <code>ZIP-PLUGIN</code> </p>"""
    package_vending_options: NotRequired[
        "aws_sdk_opensearch.types.package_vending_options.PackageVendingOptions"
    ]
    """<p> The vending options for the package being created. They determine if the package can be vended to other users.</p>"""
    package_encryption_options: NotRequired[
        "aws_sdk_opensearch.types.package_encryption_options.PackageEncryptionOptions"
    ]
    """<p>The encryption parameters for the package being created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    import aws_sdk_opensearch.types.package_type

    out["PackageType"] = aws_sdk_opensearch.types.package_type.serialize_json(
        value["package_type"]
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    import aws_sdk_opensearch.types.package_source

    out["PackageSource"] = aws_sdk_opensearch.types.package_source.serialize_json(
        value["package_source"]
    )
    if "package_configuration" in value:
        import aws_sdk_opensearch.types.package_configuration

        out["PackageConfiguration"] = (
            aws_sdk_opensearch.types.package_configuration.serialize_json(
                value["package_configuration"]
            )
        )
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "package_vending_options" in value:
        import aws_sdk_opensearch.types.package_vending_options

        out["PackageVendingOptions"] = (
            aws_sdk_opensearch.types.package_vending_options.serialize_json(
                value["package_vending_options"]
            )
        )
    if "package_encryption_options" in value:
        import aws_sdk_opensearch.types.package_encryption_options

        out["PackageEncryptionOptions"] = (
            aws_sdk_opensearch.types.package_encryption_options.serialize_json(
                value["package_encryption_options"]
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
        import aws_sdk_opensearch.types.package_type

        out["package_type"] = aws_sdk_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_type required")
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "PackageSource" in data:
        import aws_sdk_opensearch.types.package_source

        out["package_source"] = (
            aws_sdk_opensearch.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_source required")
    if "PackageConfiguration" in data:
        import aws_sdk_opensearch.types.package_configuration

        out["package_configuration"] = (
            aws_sdk_opensearch.types.package_configuration.deserialize_json(
                data["PackageConfiguration"]
            )
        )
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "PackageVendingOptions" in data:
        import aws_sdk_opensearch.types.package_vending_options

        out["package_vending_options"] = (
            aws_sdk_opensearch.types.package_vending_options.deserialize_json(
                data["PackageVendingOptions"]
            )
        )
    if "PackageEncryptionOptions" in data:
        import aws_sdk_opensearch.types.package_encryption_options

        out["package_encryption_options"] = (
            aws_sdk_opensearch.types.package_encryption_options.deserialize_json(
                data["PackageEncryptionOptions"]
            )
        )
    return out
