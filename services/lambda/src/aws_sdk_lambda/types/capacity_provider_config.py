"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config


class CapacityProviderConfig(TypedDict, closed=True):
    lambda_managed_instances_capacity_provider_config: "aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config.LambdaManagedInstancesCapacityProviderConfig"
    """<p>Configuration for Lambda-managed instances used by the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderConfig) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config

    out["LambdaManagedInstancesCapacityProviderConfig"] = (
        aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config.serialize_json(
            value["lambda_managed_instances_capacity_provider_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapacityProviderConfig:
    out: CapacityProviderConfig = {}  # type: ignore[typeddict-item]
    if "LambdaManagedInstancesCapacityProviderConfig" in data:
        import aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config

        out["lambda_managed_instances_capacity_provider_config"] = (
            aws_sdk_lambda.types.lambda_managed_instances_capacity_provider_config.deserialize_json(
                data["LambdaManagedInstancesCapacityProviderConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CapacityProviderConfig.lambda_managed_instances_capacity_provider_config required"
        )
    return out
