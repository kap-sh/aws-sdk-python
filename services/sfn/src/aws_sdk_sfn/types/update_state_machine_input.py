"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.definition
    import aws_sdk_sfn.types.encryption_configuration
    import aws_sdk_sfn.types.logging_configuration
    import aws_sdk_sfn.types.publish
    import aws_sdk_sfn.types.tracing_configuration
    import aws_sdk_sfn.types.version_description


class UpdateStateMachineInput(TypedDict):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine.</p>"""
    definition: NotRequired["aws_sdk_sfn.types.definition.Definition"]
    r"""<p>The Amazon States Language definition of the state machine. See <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\">Amazon States Language</a>.</p>"""
    role_arn: NotRequired["aws_sdk_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role of the state machine.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Use the <code>LoggingConfiguration</code> data type to set CloudWatch Logs options.</p>"""
    tracing_configuration: NotRequired[
        "aws_sdk_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    publish: "aws_sdk_sfn.types.publish.Publish"
    """<p>Specifies whether the state machine version is published. The default is <code>false</code>. To publish a version after updating the state machine, set <code>publish</code> to <code>true</code>.</p>"""
    version_description: NotRequired[
        "aws_sdk_sfn.types.version_description.VersionDescription"
    ]
    """<p>An optional description of the state machine version to publish.</p> <p>You can only specify the <code>versionDescription</code> parameter if you've set <code>publish</code> to <code>true</code>.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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
    out["publish"] = value.get("publish", False)
    if "version_description" in value:
        out["versionDescription"] = value["version_description"]
    if "encryption_configuration" in value:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineInput:
    out: UpdateStateMachineInput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("UpdateStateMachineInput.state_machine_arn required")
    if "definition" in data:
        out["definition"] = data["definition"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
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
    if "publish" in data:
        out["publish"] = data["publish"]
    else:
        out["publish"] = False
    if "versionDescription" in data:
        out["version_description"] = data["versionDescription"]
    if "encryptionConfiguration" in data:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
