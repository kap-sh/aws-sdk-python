"""Generated from Smithy shape ``com.amazonaws.batch#QuotaSharePreemptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_in_share_preemption_state


class QuotaSharePreemptionConfiguration(TypedDict, closed=True):
    in_share_preemption: NotRequired[
        "aws_sdk_batch.types.quota_share_in_share_preemption_state.QuotaShareInSharePreemptionState"
    ]
    """<p>Specifies whether jobs within a quota share can be preempted by another, higher priority job in the same quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaSharePreemptionConfiguration) -> dict:
    out: dict = {}
    if "in_share_preemption" in value:
        import aws_sdk_batch.types.quota_share_in_share_preemption_state

        out["inSharePreemption"] = (
            aws_sdk_batch.types.quota_share_in_share_preemption_state.serialize_json(
                value["in_share_preemption"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuotaSharePreemptionConfiguration:
    out: QuotaSharePreemptionConfiguration = {}  # type: ignore[typeddict-item]
    if "inSharePreemption" in data:
        import aws_sdk_batch.types.quota_share_in_share_preemption_state

        out["in_share_preemption"] = (
            aws_sdk_batch.types.quota_share_in_share_preemption_state.deserialize_json(
                data["inSharePreemption"]
            )
        )
    return out
