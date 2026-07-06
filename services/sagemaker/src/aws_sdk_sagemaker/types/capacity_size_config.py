"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacitySizeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.node_unavailability_type
    import aws_sdk_sagemaker.types.node_unavailability_value


class CapacitySizeConfig(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_sagemaker.types.node_unavailability_type.NodeUnavailabilityType"
    ]
    """<p>Specifies whether SageMaker should process the update by amount or percentage of instances.</p>"""
    value: NotRequired[
        "aws_sdk_sagemaker.types.node_unavailability_value.NodeUnavailabilityValue"
    ]
    """<p>Specifies the amount or percentage of instances SageMaker updates at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacitySizeConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_sagemaker.types.node_unavailability_type

        out["Type"] = (
            aws_sdk_sagemaker.types.node_unavailability_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacitySizeConfig:
    out: CapacitySizeConfig = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_sagemaker.types.node_unavailability_type

        out["type"] = (
            aws_sdk_sagemaker.types.node_unavailability_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
