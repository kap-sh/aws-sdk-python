"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapePoolOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.pool_arn


class DeleteTapePoolOutput(TypedDict, closed=True):
    pool_arn: NotRequired["aws_sdk_storage_gateway.types.pool_arn.PoolARN"]
    """<p>The Amazon Resource Name (ARN) of the custom tape pool being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapePoolOutput) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolARN"] = value["pool_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapePoolOutput:
    out: DeleteTapePoolOutput = {}  # type: ignore[typeddict-item]
    if "PoolARN" in data:
        out["pool_arn"] = data["PoolARN"]
    return out
