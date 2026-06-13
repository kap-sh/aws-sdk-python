"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobDirectAnalysisConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_receiver_account_ids


class ProtectedJobDirectAnalysisConfigurationDetails(TypedDict):
    receiver_account_ids: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_receiver_account_ids.ProtectedJobReceiverAccountIds"
    ]
    """<p> The receiver account IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobDirectAnalysisConfigurationDetails) -> dict:
    out: dict = {}
    if "receiver_account_ids" in value:
        import aws_sdk_cleanrooms.types.protected_job_receiver_account_ids

        out["receiverAccountIds"] = (
            aws_sdk_cleanrooms.types.protected_job_receiver_account_ids.serialize_json(
                value["receiver_account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobDirectAnalysisConfigurationDetails:
    out: ProtectedJobDirectAnalysisConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "receiverAccountIds" in data:
        import aws_sdk_cleanrooms.types.protected_job_receiver_account_ids

        out["receiver_account_ids"] = (
            aws_sdk_cleanrooms.types.protected_job_receiver_account_ids.deserialize_json(
                data["receiverAccountIds"]
            )
        )
    return out
