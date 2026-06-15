"""Generated from Smithy shape ``com.amazonaws.appconfig#HostedConfigurationVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.string_with_length_between1_and255
    import aws_sdk_appconfig.types.version_label


class HostedConfigurationVersionSummary(TypedDict):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    configuration_profile_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The configuration version.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the configuration.</p>"""
    content_type: NotRequired[
        "aws_sdk_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255"
    ]
    r"""<p>A standard MIME type describing the format of the configuration content. For more information, see <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\">Content-Type</a>.</p>"""
    version_label: NotRequired["aws_sdk_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""
    kms_key_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key that was used to encrypt this specific version of the configuration data in the AppConfig hosted configuration store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostedConfigurationVersionSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "configuration_profile_id" in value:
        out["ConfigurationProfileId"] = value["configuration_profile_id"]
    out["VersionNumber"] = value.get("version_number", 0)
    if "description" in value:
        out["Description"] = value["description"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "version_label" in value:
        out["VersionLabel"] = value["version_label"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> HostedConfigurationVersionSummary:
    out: HostedConfigurationVersionSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ConfigurationProfileId" in data:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if "Description" in data:
        out["description"] = data["Description"]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "VersionLabel" in data:
        out["version_label"] = data["VersionLabel"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
