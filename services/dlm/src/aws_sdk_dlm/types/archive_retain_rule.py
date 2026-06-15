"""Generated from Smithy shape ``com.amazonaws.dlm#ArchiveRetainRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.retention_archive_tier


class ArchiveRetainRule(TypedDict):
    retention_archive_tier: NotRequired[
        "aws_sdk_dlm.types.retention_archive_tier.RetentionArchiveTier"
    ]
    r"""<p>Information about retention period in the Amazon EBS Snapshots Archive. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html\">Archive Amazon EBS snapshots</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRetainRule) -> dict:
    out: dict = {}
    if "retention_archive_tier" in value:
        import aws_sdk_dlm.types.retention_archive_tier

        out["RetentionArchiveTier"] = (
            aws_sdk_dlm.types.retention_archive_tier.serialize_json(
                value["retention_archive_tier"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArchiveRetainRule:
    out: ArchiveRetainRule = {}  # type: ignore[typeddict-item]
    if "RetentionArchiveTier" in data:
        import aws_sdk_dlm.types.retention_archive_tier

        out["retention_archive_tier"] = (
            aws_sdk_dlm.types.retention_archive_tier.deserialize_json(
                data["RetentionArchiveTier"]
            )
        )
    return out
