"""Generated from Smithy shape ``com.amazonaws.batch#DeleteSchedulingPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteSchedulingPolicyRequest(TypedDict):
    arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the scheduling policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchedulingPolicyRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteSchedulingPolicyRequest:
    out: DeleteSchedulingPolicyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
