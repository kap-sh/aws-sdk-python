"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_name
    import capo_lambda.types.capacity_provider_scaling_config


class UpdateCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider_name: (
        "capo_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider to update.</p>"""
    capacity_provider_scaling_config: NotRequired[
        "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
    ]
    """<p>The updated scaling configuration for the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapacityProviderRequest) -> dict:
    out: dict = {}
    if "capacity_provider_scaling_config" in value:
        import capo_lambda.types.capacity_provider_scaling_config

        out["CapacityProviderScalingConfig"] = (
            capo_lambda.types.capacity_provider_scaling_config.serialize_json(
                value["capacity_provider_scaling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCapacityProviderRequest:
    out: UpdateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if "CapacityProviderScalingConfig" in data:
        import capo_lambda.types.capacity_provider_scaling_config

        out["capacity_provider_scaling_config"] = (
            capo_lambda.types.capacity_provider_scaling_config.deserialize_json(
                data["CapacityProviderScalingConfig"]
            )
        )
    return out
