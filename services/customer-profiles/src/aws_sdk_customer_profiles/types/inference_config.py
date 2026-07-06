"""Generated from Smithy shape ``com.amazonaws.customerprofiles#InferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.inference_config_min_provisioned_tps_integer


class InferenceConfig(TypedDict, closed=True):
    min_provisioned_tps: NotRequired[
        "aws_sdk_customer_profiles.types.inference_config_min_provisioned_tps_integer.InferenceConfigMinProvisionedTPSInteger"
    ]
    """<p>The minimum provisioned transactions per second (TPS) that the recommender supports. The default value is 1. A high MinProvisionedTPS will increase your cost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfig) -> dict:
    out: dict = {}
    if "min_provisioned_tps" in value:
        out["MinProvisionedTPS"] = value["min_provisioned_tps"]
    return out


def deserialize_json(data: dict) -> InferenceConfig:
    out: InferenceConfig = {}  # type: ignore[typeddict-item]
    if "MinProvisionedTPS" in data:
        out["min_provisioned_tps"] = data["MinProvisionedTPS"]
    return out
