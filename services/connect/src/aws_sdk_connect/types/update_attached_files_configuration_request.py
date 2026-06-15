"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAttachedFilesConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attachment_scope
    import aws_sdk_connect.types.extension_configuration
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.maximum_size_limit_in_bytes


class UpdateAttachedFilesConfigurationRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    attachment_scope: "aws_sdk_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment. Valid values are <code>EMAIL</code>, <code>CHAT</code>, <code>CASE</code>, and <code>TASK</code>.</p>"""
    maximum_size_limit_in_bytes: NotRequired[
        "aws_sdk_connect.types.maximum_size_limit_in_bytes.MaximumSizeLimitInBytes"
    ]
    """<p>The maximum size limit for attached files in bytes. The minimum value is 1 and the maximum value is 104857600 (100 MB).</p>"""
    extension_configuration: NotRequired[
        "aws_sdk_connect.types.extension_configuration.ExtensionConfiguration"
    ]
    """<p>The configuration for allowed file extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttachedFilesConfigurationRequest) -> dict:
    out: dict = {}
    if "maximum_size_limit_in_bytes" in value:
        out["MaximumSizeLimitInBytes"] = value["maximum_size_limit_in_bytes"]
    if "extension_configuration" in value:
        import aws_sdk_connect.types.extension_configuration

        out["ExtensionConfiguration"] = (
            aws_sdk_connect.types.extension_configuration.serialize_json(
                value["extension_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAttachedFilesConfigurationRequest:
    out: UpdateAttachedFilesConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "MaximumSizeLimitInBytes" in data:
        out["maximum_size_limit_in_bytes"] = data["MaximumSizeLimitInBytes"]
    if "ExtensionConfiguration" in data:
        import aws_sdk_connect.types.extension_configuration

        out["extension_configuration"] = (
            aws_sdk_connect.types.extension_configuration.deserialize_json(
                data["ExtensionConfiguration"]
            )
        )
    return out
