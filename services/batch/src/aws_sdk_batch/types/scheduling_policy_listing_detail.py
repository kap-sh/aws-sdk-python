"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyListingDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class SchedulingPolicyListingDetail(TypedDict):
    arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the scheduling policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyListingDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SchedulingPolicyListingDetail:
    out: SchedulingPolicyListingDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
