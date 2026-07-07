"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportDiskImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_logging_configuration
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.os_version
    import aws_sdk_imagebuilder.types.register_image_options
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.role_name_or_arn
    import aws_sdk_imagebuilder.types.tag_map
    import aws_sdk_imagebuilder.types.uri
    import aws_sdk_imagebuilder.types.version_number
    import aws_sdk_imagebuilder.types.windows_configuration


class ImportDiskImageRequest(TypedDict, closed=True):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the image resource that's created from the import.</p>"""
    semantic_version: "aws_sdk_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version to attach to the image that's created during the import process. This version follows the semantic version syntax.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description for your disk image import.</p>"""
    platform: "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The operating system platform for the imported image. Allowed values include the following: <code>Windows</code>.</p>"""
    os_version: "aws_sdk_imagebuilder.types.os_version.OsVersion"
    """<p>The operating system version for the imported image. Allowed values include the following: <code>Microsoft Windows 11</code>.</p>"""
    execution_role: NotRequired[
        "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions to import an image from a Microsoft ISO file.</p>"""
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration resource that's used for launching the EC2 instance on which the ISO image is built.</p>"""
    uri: "aws_sdk_imagebuilder.types.uri.Uri"
    """<p>The <code>uri</code> of the ISO disk file that's stored in Amazon S3.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>Define logging configuration for the image build process.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to image resources created from the import.</p>"""
    register_image_options: NotRequired[
        "aws_sdk_imagebuilder.types.register_image_options.RegisterImageOptions"
    ]
    """<p>Configures Secure Boot and UEFI settings for the imported image.</p>"""
    windows_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.windows_configuration.WindowsConfiguration"
    ]
    """<p>Specifies Windows settings for ISO imports.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDiskImageRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    out["platform"] = value["platform"]
    out["osVersion"] = value["os_version"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    out["uri"] = value["uri"]
    if "logging_configuration" in value:
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "register_image_options" in value:
        import aws_sdk_imagebuilder.types.register_image_options

        out["registerImageOptions"] = (
            aws_sdk_imagebuilder.types.register_image_options.serialize_json(
                value["register_image_options"]
            )
        )
    if "windows_configuration" in value:
        import aws_sdk_imagebuilder.types.windows_configuration

        out["windowsConfiguration"] = (
            aws_sdk_imagebuilder.types.windows_configuration.serialize_json(
                value["windows_configuration"]
            )
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportDiskImageRequest:
    out: ImportDiskImageRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportDiskImageRequest.name required")
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportDiskImageRequest.semantic_version required")
    if "description" in data:
        out["description"] = data["description"]
    if "platform" in data:
        out["platform"] = data["platform"]
    else:
        raise DeserializationError("ImportDiskImageRequest.platform required")
    if "osVersion" in data:
        out["os_version"] = data["osVersion"]
    else:
        raise DeserializationError("ImportDiskImageRequest.os_version required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "infrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "ImportDiskImageRequest.infrastructure_configuration_arn required"
        )
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("ImportDiskImageRequest.uri required")
    if "loggingConfiguration" in data:
        import aws_sdk_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            aws_sdk_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "registerImageOptions" in data:
        import aws_sdk_imagebuilder.types.register_image_options

        out["register_image_options"] = (
            aws_sdk_imagebuilder.types.register_image_options.deserialize_json(
                data["registerImageOptions"]
            )
        )
    if "windowsConfiguration" in data:
        import aws_sdk_imagebuilder.types.windows_configuration

        out["windows_configuration"] = (
            aws_sdk_imagebuilder.types.windows_configuration.deserialize_json(
                data["windowsConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ImportDiskImageRequest.client_token required")
    return out
