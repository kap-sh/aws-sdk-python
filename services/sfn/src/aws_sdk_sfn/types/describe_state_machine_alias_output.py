"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineAliasOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.alias_description
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.routing_configuration_list
    import aws_sdk_sfn.types.timestamp


class DescribeStateMachineAliasOutput(TypedDict):
    state_machine_alias_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine alias.</p>"""
    name: NotRequired["aws_sdk_sfn.types.name.Name"]
    """<p>The name of the state machine alias.</p>"""
    description: NotRequired["aws_sdk_sfn.types.alias_description.AliasDescription"]
    """<p>A description of the alias.</p>"""
    routing_configuration: NotRequired[
        "aws_sdk_sfn.types.routing_configuration_list.RoutingConfigurationList"
    ]
    """<p>The routing configuration of the alias.</p>"""
    creation_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date the state machine alias was created.</p>"""
    update_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date the state machine alias was last updated.</p> <p>For a newly created state machine, this is the same as the creation date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineAliasOutput) -> dict:
    out: dict = {}
    if "state_machine_alias_arn" in value:
        out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import aws_sdk_sfn.types.routing_configuration_list

        out["routingConfiguration"] = (
            aws_sdk_sfn.types.routing_configuration_list.serialize_aws_json_1_0(
                value["routing_configuration"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["creation_date"]
        )
    if "update_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["updateDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["update_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineAliasOutput:
    out: DescribeStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
    if "stateMachineAliasArn" in data:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_sfn.types.routing_configuration_list

        out["routing_configuration"] = (
            aws_sdk_sfn.types.routing_configuration_list.deserialize_aws_json_1_0(
                data["routingConfiguration"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    if "updateDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["update_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    return out
