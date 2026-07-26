"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapeArchiveOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.tape_arn


class DeleteTapeArchiveOutput(TypedDict, closed=True):
    tape_arn: NotRequired["capo_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape shelf (VTS).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapeArchiveOutput) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapeArchiveOutput:
    out: DeleteTapeArchiveOutput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    return out
