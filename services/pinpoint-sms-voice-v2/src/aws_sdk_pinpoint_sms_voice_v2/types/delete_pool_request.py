"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeletePoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn


class DeletePoolRequest(TypedDict):
    pool_id: "aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    """<p>The PoolId or PoolArn of the pool to delete. You can use <a>DescribePools</a> to find the values for PoolId and PoolArn .</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePoolRequest:
    out: DeletePoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("DeletePoolRequest.pool_id required")
    return out
