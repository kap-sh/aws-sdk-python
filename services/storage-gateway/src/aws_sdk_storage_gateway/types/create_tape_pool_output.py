"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateTapePoolOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.pool_arn


class CreateTapePoolOutput(TypedDict):
    pool_arn: NotRequired["aws_sdk_storage_gateway.types.pool_arn.PoolARN"]
    """<p>The unique Amazon Resource Name (ARN) that represents the custom tape pool. Use the <a>ListTapePools</a> operation to return a list of tape pools for your account and Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTapePoolOutput) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolARN"] = value["pool_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTapePoolOutput:
    out: CreateTapePoolOutput = {}  # type: ignore[typeddict-item]
    if "PoolARN" in data:
        out["pool_arn"] = data["PoolARN"]
    return out
