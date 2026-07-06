"""Generated from Smithy shape ``com.amazonaws.batch#CreateSchedulingPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class CreateSchedulingPolicyResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the scheduling policy.</p>"""
    arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the scheduling policy. The format is <code>aws:<i>Partition</i>:batch:<i>Region</i>:<i>Account</i>:scheduling-policy/<i>Name</i> </code>. For example, <code>aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchedulingPolicyResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateSchedulingPolicyResponse:
    out: CreateSchedulingPolicyResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
