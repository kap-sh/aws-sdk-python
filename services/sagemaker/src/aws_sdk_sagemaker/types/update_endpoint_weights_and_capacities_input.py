"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateEndpointWeightsAndCapacitiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.desired_weight_and_capacity_list
    import aws_sdk_sagemaker.types.endpoint_name


class UpdateEndpointWeightsAndCapacitiesInput(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of an existing SageMaker endpoint.</p>"""
    desired_weights_and_capacities: NotRequired[
        "aws_sdk_sagemaker.types.desired_weight_and_capacity_list.DesiredWeightAndCapacityList"
    ]
    """<p>An object that provides new capacity and weight values for a variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointWeightsAndCapacitiesInput) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "desired_weights_and_capacities" in value:
        import aws_sdk_sagemaker.types.desired_weight_and_capacity_list

        out["DesiredWeightsAndCapacities"] = (
            aws_sdk_sagemaker.types.desired_weight_and_capacity_list.serialize_aws_json_1_1(
                value["desired_weights_and_capacities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointWeightsAndCapacitiesInput:
    out: UpdateEndpointWeightsAndCapacitiesInput = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "DesiredWeightsAndCapacities" in data:
        import aws_sdk_sagemaker.types.desired_weight_and_capacity_list

        out["desired_weights_and_capacities"] = (
            aws_sdk_sagemaker.types.desired_weight_and_capacity_list.deserialize_aws_json_1_1(
                data["DesiredWeightsAndCapacities"]
            )
        )
    return out
