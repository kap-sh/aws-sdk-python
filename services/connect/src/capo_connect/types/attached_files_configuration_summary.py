"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.attachment_scope
    import capo_connect.types.extension_configuration
    import capo_connect.types.instance_id
    import capo_connect.types.maximum_size_limit_in_bytes


class AttachedFilesConfigurationSummary(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    attachment_scope: "capo_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment. Valid values are <code>EMAIL</code>, <code>CHAT</code>, <code>CASE</code>, and <code>TASK</code>.</p>"""
    maximum_size_limit_in_bytes: NotRequired[
        "capo_connect.types.maximum_size_limit_in_bytes.MaximumSizeLimitInBytes"
    ]
    extension_configuration: NotRequired[
        "capo_connect.types.extension_configuration.ExtensionConfiguration"
    ]
    """<p>The configuration for allowed file extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesConfigurationSummary) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.attachment_scope

    out["AttachmentScope"] = capo_connect.types.attachment_scope.serialize_json(
        value["attachment_scope"]
    )
    if "maximum_size_limit_in_bytes" in value:
        out["MaximumSizeLimitInBytes"] = value["maximum_size_limit_in_bytes"]
    if "extension_configuration" in value:
        import capo_connect.types.extension_configuration

        out["ExtensionConfiguration"] = (
            capo_connect.types.extension_configuration.serialize_json(
                value["extension_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttachedFilesConfigurationSummary:
    out: AttachedFilesConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "AttachedFilesConfigurationSummary.instance_id required"
        )
    if "AttachmentScope" in data:
        import capo_connect.types.attachment_scope

        out["attachment_scope"] = capo_connect.types.attachment_scope.deserialize_json(
            data["AttachmentScope"]
        )
    else:
        raise DeserializationError(
            "AttachedFilesConfigurationSummary.attachment_scope required"
        )
    if "MaximumSizeLimitInBytes" in data:
        out["maximum_size_limit_in_bytes"] = data["MaximumSizeLimitInBytes"]
    if "ExtensionConfiguration" in data:
        import capo_connect.types.extension_configuration

        out["extension_configuration"] = (
            capo_connect.types.extension_configuration.deserialize_json(
                data["ExtensionConfiguration"]
            )
        )
    return out
