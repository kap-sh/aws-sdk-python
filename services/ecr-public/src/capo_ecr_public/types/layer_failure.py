"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.batched_operation_layer_digest
    import capo_ecr_public.types.layer_failure_code
    import capo_ecr_public.types.layer_failure_reason


class LayerFailure(TypedDict, closed=True):
    layer_digest: NotRequired[
        "capo_ecr_public.types.batched_operation_layer_digest.BatchedOperationLayerDigest"
    ]
    """<p>The layer digest that's associated with the failure.</p>"""
    failure_code: NotRequired[
        "capo_ecr_public.types.layer_failure_code.LayerFailureCode"
    ]
    """<p>The failure code that's associated with the failure.</p>"""
    failure_reason: NotRequired[
        "capo_ecr_public.types.layer_failure_reason.LayerFailureReason"
    ]
    """<p>The reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerFailure) -> dict:
    out: dict = {}
    if "layer_digest" in value:
        out["layerDigest"] = value["layer_digest"]
    if "failure_code" in value:
        import capo_ecr_public.types.layer_failure_code

        out["failureCode"] = (
            capo_ecr_public.types.layer_failure_code.serialize_aws_json_1_1(
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
        import capo_ecr_public.types.layer_failure_code

        out["failure_code"] = (
            capo_ecr_public.types.layer_failure_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
