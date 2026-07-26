"""Generated from Smithy shape ``com.amazonaws.fsx#BackupFailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class BackupFailureDetails(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]
    """<p>A message describing the backup-creation failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupFailureDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupFailureDetails:
    out: BackupFailureDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
