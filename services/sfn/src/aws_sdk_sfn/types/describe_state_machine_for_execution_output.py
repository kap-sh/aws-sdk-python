"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineForExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.definition
    import aws_sdk_sfn.types.encryption_configuration
    import aws_sdk_sfn.types.logging_configuration
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.map_run_label
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.revision_id
    import aws_sdk_sfn.types.timestamp
    import aws_sdk_sfn.types.tracing_configuration
    import aws_sdk_sfn.types.variable_references


class DescribeStateMachineForExecutionOutput(TypedDict, closed=True):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine associated with the execution.</p>"""
    name: "aws_sdk_sfn.types.name.Name"
    """<p>The name of the state machine associated with the execution.</p>"""
    definition: "aws_sdk_sfn.types.definition.Definition"
    r"""<p>The Amazon States Language definition of the state machine. See <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\">Amazon States Language</a>.</p>"""
    role_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role of the State Machine for the execution. </p>"""
    update_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date and time the state machine associated with an execution was updated. For a newly created state machine, this is the creation date.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    tracing_configuration: NotRequired[
        "aws_sdk_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    map_run_arn: NotRequired["aws_sdk_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the Map Run that started the child workflow execution. This field is returned only if the <code>executionArn</code> is a child workflow execution that was started by a Distributed Map state.</p>"""
    label: NotRequired["aws_sdk_sfn.types.map_run_label.MapRunLabel"]
    """<p>A user-defined or an auto-generated string that identifies a <code>Map</code> state. This field is returned only if the <code>executionArn</code> is a child workflow execution that was started by a Distributed Map state.</p>"""
    revision_id: NotRequired["aws_sdk_sfn.types.revision_id.RevisionId"]
    """<p>The revision identifier for the state machine. The first revision ID when you create the state machine is null.</p> <p>Use the state machine <code>revisionId</code> parameter to compare the revision of a state machine with the configuration of the state machine used for executions without performing a diff of the properties, such as <code>definition</code> and <code>roleArn</code>.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption. </p>"""
    variable_references: NotRequired[
        "aws_sdk_sfn.types.variable_references.VariableReferences"
    ]
    """<p>A map of <b>state name</b> to a list of variables referenced by that state. States that do not use variable references will not be shown in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineForExecutionOutput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    out["roleArn"] = value["role_arn"]
    import aws_sdk_sfn.types.timestamp

    out["updateDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["update_date"]
    )
    if "logging_configuration" in value:
        import aws_sdk_sfn.types.logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_sfn.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "tracing_configuration" in value:
        import aws_sdk_sfn.types.tracing_configuration

        out["tracingConfiguration"] = (
            aws_sdk_sfn.types.tracing_configuration.serialize_aws_json_1_0(
                value["tracing_configuration"]
            )
        )
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    if "label" in value:
        out["label"] = value["label"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "encryption_configuration" in value:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "variable_references" in value:
        import aws_sdk_sfn.types.variable_references

        out["variableReferences"] = (
            aws_sdk_sfn.types.variable_references.serialize_aws_json_1_0(
                value["variable_references"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineForExecutionOutput:
    out: DescribeStateMachineForExecutionOutput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError(
            "DescribeStateMachineForExecutionOutput.state_machine_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DescribeStateMachineForExecutionOutput.name required"
        )
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError(
            "DescribeStateMachineForExecutionOutput.definition required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "DescribeStateMachineForExecutionOutput.role_arn required"
        )
    if "updateDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["update_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["updateDate"]
        )
    else:
        raise DeserializationError(
            "DescribeStateMachineForExecutionOutput.update_date required"
        )
    if "loggingConfiguration" in data:
        import aws_sdk_sfn.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_sfn.types.logging_configuration.deserialize_aws_json_1_0(
                data["loggingConfiguration"]
            )
        )
    if "tracingConfiguration" in data:
        import aws_sdk_sfn.types.tracing_configuration

        out["tracing_configuration"] = (
            aws_sdk_sfn.types.tracing_configuration.deserialize_aws_json_1_0(
                data["tracingConfiguration"]
            )
        )
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    if "label" in data:
        out["label"] = data["label"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "encryptionConfiguration" in data:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    if "variableReferences" in data:
        import aws_sdk_sfn.types.variable_references

        out["variable_references"] = (
            aws_sdk_sfn.types.variable_references.deserialize_aws_json_1_0(
                data["variableReferences"]
            )
        )
    return out
