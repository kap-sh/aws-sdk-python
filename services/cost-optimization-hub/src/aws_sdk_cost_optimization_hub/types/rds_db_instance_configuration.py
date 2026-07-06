"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RdsDbInstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.db_instance_configuration


class RdsDbInstanceConfiguration(TypedDict, closed=True):
    instance: NotRequired[
        "aws_sdk_cost_optimization_hub.types.db_instance_configuration.DbInstanceConfiguration"
    ]
    """<p>Details about the instance configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsDbInstanceConfiguration) -> dict:
    out: dict = {}
    if "instance" in value:
        import aws_sdk_cost_optimization_hub.types.db_instance_configuration

        out["instance"] = (
            aws_sdk_cost_optimization_hub.types.db_instance_configuration.serialize_aws_json_1_0(
                value["instance"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsDbInstanceConfiguration:
    out: RdsDbInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import aws_sdk_cost_optimization_hub.types.db_instance_configuration

        out["instance"] = (
            aws_sdk_cost_optimization_hub.types.db_instance_configuration.deserialize_aws_json_1_0(
                data["instance"]
            )
        )
    return out
