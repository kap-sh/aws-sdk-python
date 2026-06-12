"""Generated from Smithy shape ``com.amazonaws.storagegateway#AssignTapePoolOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_arn


class AssignTapePoolOutput(TypedDict):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignTapePoolOutput) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssignTapePoolOutput:
    out: AssignTapePoolOutput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    return out
