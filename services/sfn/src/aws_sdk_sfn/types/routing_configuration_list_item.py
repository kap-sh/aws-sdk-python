"""Generated from Smithy shape ``com.amazonaws.sfn#RoutingConfigurationListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.version_weight


class RoutingConfigurationListItem(TypedDict):
    state_machine_version_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.</p> <p>If you specify the ARN of a second version, it must belong to the same state machine as the first version.</p>"""
    weight: "aws_sdk_sfn.types.version_weight.VersionWeight"
    """<p>The percentage of traffic you want to route to a state machine version. The sum of the weights in the routing configuration must be equal to 100.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingConfigurationListItem) -> dict:
    out: dict = {}
    out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    out["weight"] = value.get("weight", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> RoutingConfigurationListItem:
    out: RoutingConfigurationListItem = {}  # type: ignore[typeddict-item]
    if "stateMachineVersionArn" in data:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    else:
        raise DeserializationError(
            "RoutingConfigurationListItem.state_machine_version_arn required"
        )
    if "weight" in data:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    return out
