"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobDirectAnalysisConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_receiver_account_ids


class ProtectedJobDirectAnalysisConfigurationDetails(TypedDict, closed=True):
    receiver_account_ids: NotRequired[
        "capo_cleanrooms.types.protected_job_receiver_account_ids.ProtectedJobReceiverAccountIds"
    ]
    """<p> The receiver account IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobDirectAnalysisConfigurationDetails) -> dict:
    out: dict = {}
    if "receiver_account_ids" in value:
        import capo_cleanrooms.types.protected_job_receiver_account_ids

        out["receiverAccountIds"] = (
            capo_cleanrooms.types.protected_job_receiver_account_ids.serialize_json(
                value["receiver_account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobDirectAnalysisConfigurationDetails:
    out: ProtectedJobDirectAnalysisConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "receiverAccountIds" in data:
        import capo_cleanrooms.types.protected_job_receiver_account_ids

        out["receiver_account_ids"] = (
            capo_cleanrooms.types.protected_job_receiver_account_ids.deserialize_json(
                data["receiverAccountIds"]
            )
        )
    return out
