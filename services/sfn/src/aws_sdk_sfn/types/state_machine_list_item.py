"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.state_machine_type
    import aws_sdk_sfn.types.timestamp


class StateMachineListItem(TypedDict):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the state machine.</p>"""
    name: "aws_sdk_sfn.types.name.Name"
    """<p>The name of the state machine.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    type: "aws_sdk_sfn.types.state_machine_type.StateMachineType"
    """<p></p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine is created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineListItem) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    out["name"] = value["name"]
    import aws_sdk_sfn.types.state_machine_type

    out["type"] = aws_sdk_sfn.types.state_machine_type.serialize_aws_json_1_0(
        value["type"]
    )
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateMachineListItem:
    out: StateMachineListItem = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("StateMachineListItem.state_machine_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StateMachineListItem.name required")
    if "type" in data:
        import aws_sdk_sfn.types.state_machine_type

        out["type"] = aws_sdk_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("StateMachineListItem.type required")
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("StateMachineListItem.creation_date required")
    return out
