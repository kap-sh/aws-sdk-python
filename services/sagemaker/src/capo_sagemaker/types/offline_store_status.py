"""Generated from Smithy shape ``com.amazonaws.sagemaker#OfflineStoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.blocked_reason
    import capo_sagemaker.types.offline_store_status_value


class OfflineStoreStatus(TypedDict, closed=True):
    status: NotRequired[
        "capo_sagemaker.types.offline_store_status_value.OfflineStoreStatusValue"
    ]
    """<p>An <code>OfflineStore</code> status.</p>"""
    blocked_reason: NotRequired["capo_sagemaker.types.blocked_reason.BlockedReason"]
    """<p>The justification for why the OfflineStoreStatus is Blocked (if applicable).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfflineStoreStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sagemaker.types.offline_store_status_value

        out["Status"] = (
            capo_sagemaker.types.offline_store_status_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "blocked_reason" in value:
        out["BlockedReason"] = value["blocked_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OfflineStoreStatus:
    out: OfflineStoreStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_sagemaker.types.offline_store_status_value

        out["status"] = (
            capo_sagemaker.types.offline_store_status_value.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "BlockedReason" in data:
        out["blocked_reason"] = data["BlockedReason"]
    return out
