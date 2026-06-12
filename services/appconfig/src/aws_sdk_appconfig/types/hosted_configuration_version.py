"""Generated from Smithy shape ``com.amazonaws.appconfig#HostedConfigurationVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.blob
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.string_with_length_between1_and255
    import aws_sdk_appconfig.types.version_label


class HostedConfigurationVersion(TypedDict):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    configuration_profile_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The configuration version.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p>"""
    content: NotRequired["aws_sdk_appconfig.types.blob.Blob"]
    """<p>The content of the configuration or the configuration data.</p>"""
    content_type: NotRequired[
        "aws_sdk_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    ]
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\">Content-Type</a>.</p>"""
    version_label: NotRequired["aws_sdk_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""
    kms_key_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key that was used to encrypt this specific version of the configuration data in the AppConfig hosted configuration store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostedConfigurationVersion) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_appconfig.types.blob

        out["Content"] = aws_sdk_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> HostedConfigurationVersion:
    out: HostedConfigurationVersion = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_appconfig.types.blob

        out["content"] = aws_sdk_appconfig.types.blob.deserialize_json(data["Content"])
    return out
