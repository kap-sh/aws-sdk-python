"""Generated from Smithy shape ``com.amazonaws.storagegateway#CancelArchivalOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.tape_arn


class CancelArchivalOutput(TypedDict, closed=True):
    tape_arn: NotRequired["capo_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of the virtual tape for which archiving was canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelArchivalOutput) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelArchivalOutput:
    out: CancelArchivalOutput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    return out
