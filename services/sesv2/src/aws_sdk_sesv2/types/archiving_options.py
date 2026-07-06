"""Generated from Smithy shape ``com.amazonaws.sesv2#ArchivingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.archive_arn


class ArchivingOptions(TypedDict, closed=True):
    archive_arn: NotRequired["aws_sdk_sesv2.types.archive_arn.ArchiveArn"]
    """<p>The Amazon Resource Name (ARN) of the MailManager archive where the Amazon SES API v2 will archive sent emails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchivingOptions) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    return out


def deserialize_json(data: dict) -> ArchivingOptions:
    out: ArchivingOptions = {}  # type: ignore[typeddict-item]
    if "ArchiveArn" in data:
        out["archive_arn"] = data["ArchiveArn"]
    return out
