"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_ar_ns


class CreateTapesOutput(TypedDict):
    tape_ar_ns: NotRequired["aws_sdk_storage_gateway.types.tape_ar_ns.TapeARNs"]
    """<p>A list of unique Amazon Resource Names (ARNs) that represents the virtual tapes that were created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapesOutput) -> dict:
    out: dict = {}
    if "tape_ar_ns" in value:
        import aws_sdk_storage_gateway.types.tape_ar_ns

        out["TapeARNs"] = (
            aws_sdk_storage_gateway.types.tape_ar_ns.serialize_aws_json_1_1(
                value["tape_ar_ns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapesOutput:
    out: CreateTapesOutput = {}  # type: ignore[typeddict-item]
    if "TapeARNs" in data:
        import aws_sdk_storage_gateway.types.tape_ar_ns

        out["tape_ar_ns"] = (
            aws_sdk_storage_gateway.types.tape_ar_ns.deserialize_aws_json_1_1(
                data["TapeARNs"]
            )
        )
    return out
