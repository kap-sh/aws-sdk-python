"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetArchivingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.archive_arn
    import aws_sdk_sesv2.types.configuration_set_name


class PutConfigurationSetArchivingOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set to associate with a MailManager archive.</p>"""
    archive_arn: NotRequired["aws_sdk_sesv2.types.archive_arn.ArchiveArn"]
    """<p>The Amazon Resource Name (ARN) of the MailManager archive that the Amazon SES API v2 sends email to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetArchivingOptionsRequest) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    return out


def deserialize_json(data: dict) -> PutConfigurationSetArchivingOptionsRequest:
    out: PutConfigurationSetArchivingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveArn" in data:
        out["archive_arn"] = data["ArchiveArn"]
    return out
