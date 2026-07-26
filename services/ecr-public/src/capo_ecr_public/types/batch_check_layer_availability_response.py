"""Generated from Smithy shape ``com.amazonaws.ecrpublic#BatchCheckLayerAvailabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.layer_failure_list
    import capo_ecr_public.types.layer_list


class BatchCheckLayerAvailabilityResponse(TypedDict, closed=True):
    layers: NotRequired["capo_ecr_public.types.layer_list.LayerList"]
    """<p>A list of image layer objects that correspond to the image layer references in the request.</p>"""
    failures: NotRequired["capo_ecr_public.types.layer_failure_list.LayerFailureList"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCheckLayerAvailabilityResponse) -> dict:
    out: dict = {}
    if "layers" in value:
        import capo_ecr_public.types.layer_list

        out["layers"] = capo_ecr_public.types.layer_list.serialize_aws_json_1_1(
            value["layers"]
        )
    if "failures" in value:
        import capo_ecr_public.types.layer_failure_list

        out["failures"] = (
            capo_ecr_public.types.layer_failure_list.serialize_aws_json_1_1(
                value["failures"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCheckLayerAvailabilityResponse:
    out: BatchCheckLayerAvailabilityResponse = {}  # type: ignore[typeddict-item]
    if "layers" in data:
        import capo_ecr_public.types.layer_list

        out["layers"] = capo_ecr_public.types.layer_list.deserialize_aws_json_1_1(
            data["layers"]
        )
    if "failures" in data:
        import capo_ecr_public.types.layer_failure_list

        out["failures"] = (
            capo_ecr_public.types.layer_failure_list.deserialize_aws_json_1_1(
                data["failures"]
            )
        )
    return out
