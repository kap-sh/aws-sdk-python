"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapePoolInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.pool_arn


class DeleteTapePoolInput(TypedDict):
    pool_arn: "aws_sdk_storage_gateway.types.pool_arn.PoolARN"
    """<p>The Amazon Resource Name (ARN) of the custom tape pool to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapePoolInput) -> dict:
    out: dict = {}
    out["PoolARN"] = value["pool_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapePoolInput:
    out: DeleteTapePoolInput = {}  # type: ignore[typeddict-item]
    if "PoolARN" in data:
        out["pool_arn"] = data["PoolARN"]
    else:
        raise DeserializationError("DeleteTapePoolInput.pool_arn required")
    return out
