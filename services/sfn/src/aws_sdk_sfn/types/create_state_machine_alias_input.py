"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.alias_description
    import aws_sdk_sfn.types.character_restricted_name
    import aws_sdk_sfn.types.routing_configuration_list


class CreateStateMachineAliasInput(TypedDict, closed=True):
    description: NotRequired["aws_sdk_sfn.types.alias_description.AliasDescription"]
    """<p>A description for the state machine alias.</p>"""
    name: "aws_sdk_sfn.types.character_restricted_name.CharacterRestrictedName"
    """<p>The name of the state machine alias.</p> <p>To avoid conflict with version ARNs, don't use an integer in the name of the alias.</p>"""
    routing_configuration: (
        "aws_sdk_sfn.types.routing_configuration_list.RoutingConfigurationList"
    )
    """<p>The routing configuration of a state machine alias. The routing configuration shifts execution traffic between two state machine versions. <code>routingConfiguration</code> contains an array of <code>RoutingConfig</code> objects that specify up to two state machine versions. Step Functions then randomly choses which version to run an execution with based on the weight assigned to each <code>RoutingConfig</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineAliasInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import aws_sdk_sfn.types.routing_configuration_list

    out["routingConfiguration"] = (
        aws_sdk_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
            value["routing_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineAliasInput:
    out: CreateStateMachineAliasInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateStateMachineAliasInput.name required")
    if "routingConfiguration" in data:
        import aws_sdk_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            aws_sdk_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateStateMachineAliasInput.routing_configuration required"
        )
    return out
