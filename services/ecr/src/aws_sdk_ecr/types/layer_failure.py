"""Generated from Smithy shape ``com.amazonaws.ecr#LayerFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.batched_operation_layer_digest
    import aws_sdk_ecr.types.layer_failure_code
    import aws_sdk_ecr.types.layer_failure_reason


class LayerFailure(TypedDict):
    layer_digest: NotRequired[
        "aws_sdk_ecr.types.batched_operation_layer_digest.BatchedOperationLayerDigest"
    ]
    """<p>The layer digest associated with the failure.</p>"""
    failure_code: NotRequired["aws_sdk_ecr.types.layer_failure_code.LayerFailureCode"]
    """<p>The failure code associated with the failure.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_ecr.types.layer_failure_reason.LayerFailureReason"
    ]
    """<p>The reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerFailure) -> dict:
    out: dict = {}
    if "layer_digest" in value:
        out["layerDigest"] = value["layer_digest"]
    if "failure_code" in value:
        import aws_sdk_ecr.types.layer_failure_code

        out["failureCode"] = (
            aws_sdk_ecr.types.layer_failure_code.serialize_aws_json_1_1(
                value["failure_code"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LayerFailure:
    out: LayerFailure = {}  # type: ignore[typeddict-item]
    if "layerDigest" in data:
        out["layer_digest"] = data["layerDigest"]
    if "failureCode" in data:
        import aws_sdk_ecr.types.layer_failure_code

        out["failure_code"] = (
            aws_sdk_ecr.types.layer_failure_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
