"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAttachedFilesConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attachment_scope
    import aws_sdk_connect.types.extension_configuration
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.maximum_size_limit_in_bytes
    import aws_sdk_connect.types.timestamp


class UpdateAttachedFilesConfigurationResponse(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    attachment_scope: "aws_sdk_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment.</p>"""
    maximum_size_limit_in_bytes: NotRequired[
        "aws_sdk_connect.types.maximum_size_limit_in_bytes.MaximumSizeLimitInBytes"
    ]
    """<p>The maximum size limit for attached files in bytes.</p>"""
    extension_configuration: NotRequired[
        "aws_sdk_connect.types.extension_configuration.ExtensionConfiguration"
    ]
    """<p>The configuration for allowed file extensions.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttachedFilesConfigurationResponse) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_connect.types.attachment_scope

    out["AttachmentScope"] = aws_sdk_connect.types.attachment_scope.serialize_json(
        value["attachment_scope"]
    )
    if "maximum_size_limit_in_bytes" in value:
        out["MaximumSizeLimitInBytes"] = value["maximum_size_limit_in_bytes"]
    if "extension_configuration" in value:
        import aws_sdk_connect.types.extension_configuration

        out["ExtensionConfiguration"] = (
            aws_sdk_connect.types.extension_configuration.serialize_json(
                value["extension_configuration"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAttachedFilesConfigurationResponse:
    out: UpdateAttachedFilesConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateAttachedFilesConfigurationResponse.instance_id required"
        )
    if "AttachmentScope" in data:
        import aws_sdk_connect.types.attachment_scope

        out["attachment_scope"] = (
            aws_sdk_connect.types.attachment_scope.deserialize_json(
                data["AttachmentScope"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAttachedFilesConfigurationResponse.attachment_scope required"
        )
    if "MaximumSizeLimitInBytes" in data:
        out["maximum_size_limit_in_bytes"] = data["MaximumSizeLimitInBytes"]
    if "ExtensionConfiguration" in data:
        import aws_sdk_connect.types.extension_configuration

        out["extension_configuration"] = (
            aws_sdk_connect.types.extension_configuration.deserialize_json(
                data["ExtensionConfiguration"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
