"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapeWithBarcodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_arn


class CreateTapeWithBarcodeOutput(TypedDict, closed=True):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapeWithBarcodeOutput) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapeWithBarcodeOutput:
    out: CreateTapeWithBarcodeOutput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    return out
