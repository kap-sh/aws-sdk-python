"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.alias_description
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.routing_configuration_list


class UpdateStateMachineAliasInput(TypedDict):
    state_machine_alias_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine alias.</p>"""
    description: NotRequired["aws_sdk_sfn.types.alias_description.AliasDescription"]
    """<p>A description of the state machine alias.</p>"""
    routing_configuration: NotRequired[
        "aws_sdk_sfn.types.routing_configuration_list.RoutingConfigurationList"
    ]
    """<p>The routing configuration of the state machine alias.</p> <p>An array of <code>RoutingConfig</code> objects that specifies up to two state machine versions that the alias starts executions for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineAliasInput) -> dict:
    out: dict = {}
    out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import aws_sdk_sfn.types.routing_configuration_list

        out["routingConfiguration"] = (
            aws_sdk_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
                value["routing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineAliasInput:
    out: UpdateStateMachineAliasInput = {}  # type: ignore[typeddict-item]
    if "stateMachineAliasArn" in data:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    else:
        raise DeserializationError(
            "UpdateStateMachineAliasInput.state_machine_alias_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            aws_sdk_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    return out
