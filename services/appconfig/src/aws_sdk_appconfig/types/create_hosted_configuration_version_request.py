"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateHostedConfigurationVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.blob
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.string_with_length_between1_and255
    import aws_sdk_appconfig.types.version_label


class CreateHostedConfigurationVersionRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The configuration profile ID.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p>"""
    content: "aws_sdk_appconfig.types.blob.Blob"
    """<p>The configuration data, as bytes.</p> <note> <p>AppConfig accepts any type of data, including text formats like JSON or TOML, or binary formats like protocol buffers or compressed data.</p> </note>"""
    content_type: "aws_sdk_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\">Content-Type</a>.</p>"""
    latest_version_number: NotRequired["aws_sdk_appconfig.types.integer.Integer"]
    """<p>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</p>"""
    version_label: NotRequired["aws_sdk_appconfig.types.version_label.VersionLabel"]
    """<p>An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, \"v2.2.0\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHostedConfigurationVersionRequest) -> dict:
    out: dict = {}
    import aws_sdk_appconfig.types.blob

    out["Content"] = aws_sdk_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> CreateHostedConfigurationVersionRequest:
    out: CreateHostedConfigurationVersionRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_appconfig.types.blob

        out["content"] = aws_sdk_appconfig.types.blob.deserialize_json(data["Content"])
    else:
        raise DeserializationError(
            "CreateHostedConfigurationVersionRequest.content required"
        )
    return out
