"""Generated from Smithy shape ``com.amazonaws.sagemaker#PlacementSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.training_instance_count


class PlacementSpecification(TypedDict, closed=True):
    ultra_server_id: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The unique identifier of the UltraServer where instances should be placed.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of ML compute instances required to be placed together on the same UltraServer. Minimum value of 1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementSpecification) -> dict:
    out: dict = {}
    if "ultra_server_id" in value:
        out["UltraServerId"] = value["ultra_server_id"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementSpecification:
    out: PlacementSpecification = {}  # type: ignore[typeddict-item]
    if "UltraServerId" in data:
        out["ultra_server_id"] = data["UltraServerId"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    return out
