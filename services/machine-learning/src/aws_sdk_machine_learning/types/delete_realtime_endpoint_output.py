"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteRealtimeEndpointOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.realtime_endpoint_info


class DeleteRealtimeEndpointOutput(TypedDict):
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the <code>MLModel</code>. This value should be identical to the value of the <code>MLModelId</code> in the request.</p>"""
    realtime_endpoint_info: NotRequired[
        "aws_sdk_machine_learning.types.realtime_endpoint_info.RealtimeEndpointInfo"
    ]
    """<p>The endpoint information of the <code>MLModel</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRealtimeEndpointOutput) -> dict:
    out: dict = {}
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    if "realtime_endpoint_info" in value:
        import aws_sdk_machine_learning.types.realtime_endpoint_info

        out["RealtimeEndpointInfo"] = (
            aws_sdk_machine_learning.types.realtime_endpoint_info.serialize_aws_json_1_1(
                value["realtime_endpoint_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRealtimeEndpointOutput:
    out: DeleteRealtimeEndpointOutput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    if "RealtimeEndpointInfo" in data:
        import aws_sdk_machine_learning.types.realtime_endpoint_info

        out["realtime_endpoint_info"] = (
            aws_sdk_machine_learning.types.realtime_endpoint_info.deserialize_aws_json_1_1(
                data["RealtimeEndpointInfo"]
            )
        )
    return out
