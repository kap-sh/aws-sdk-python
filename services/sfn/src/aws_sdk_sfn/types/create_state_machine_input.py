"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.definition
    import aws_sdk_sfn.types.encryption_configuration
    import aws_sdk_sfn.types.logging_configuration
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.publish
    import aws_sdk_sfn.types.state_machine_type
    import aws_sdk_sfn.types.tag_list
    import aws_sdk_sfn.types.tracing_configuration
    import aws_sdk_sfn.types.version_description


class CreateStateMachineInput(TypedDict, closed=True):
    name: "aws_sdk_sfn.types.name.Name"
    r"""<p>The name of the state machine. </p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    definition: "aws_sdk_sfn.types.definition.Definition"
    r"""<p>The Amazon States Language definition of the state machine. See <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html\">Amazon States Language</a>.</p>"""
    role_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to use for this state machine.</p>"""
    type: NotRequired["aws_sdk_sfn.types.state_machine_type.StateMachineType"]
    """<p>Determines whether a Standard or Express state machine is created. The default is <code>STANDARD</code>. You cannot update the <code>type</code> of a state machine once it has been created.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    r"""<p>Defines what execution history events are logged and where they are logged.</p> <note> <p>By default, the <code>level</code> is set to <code>OFF</code>. For more information see <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html\">Log Levels</a> in the Step Functions User Guide.</p> </note>"""
    tags: NotRequired["aws_sdk_sfn.types.tag_list.TagList"]
    r"""<p>Tags to be added when creating a state machine.</p> <p>An array of key-value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html\">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""
    tracing_configuration: NotRequired[
        "aws_sdk_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    publish: "aws_sdk_sfn.types.publish.Publish"
    """<p>Set to <code>true</code> to publish the first version of the state machine during creation. The default is <code>false</code>.</p>"""
    version_description: NotRequired[
        "aws_sdk_sfn.types.version_description.VersionDescription"
    ]
    """<p>Sets description about the state machine version. You can only set the description if the <code>publish</code> parameter is set to <code>true</code>. Otherwise, if you set <code>versionDescription</code>, but <code>publish</code> to <code>false</code>, this API action throws <code>ValidationException</code>.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    out["roleArn"] = value["role_arn"]
    if "type" in value:
        import aws_sdk_sfn.types.state_machine_type

        out["type"] = aws_sdk_sfn.types.state_machine_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "logging_configuration" in value:
        import aws_sdk_sfn.types.logging_configuration

        out["loggingConfiguration"] = (
            aws_sdk_sfn.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
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


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineInput:
    out: CreateStateMachineInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateStateMachineInput.name required")
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("CreateStateMachineInput.definition required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateStateMachineInput.role_arn required")
    if "type" in data:
        import aws_sdk_sfn.types.state_machine_type

        out["type"] = aws_sdk_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if "loggingConfiguration" in data:
        import aws_sdk_sfn.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_sfn.types.logging_configuration.deserialize_aws_json_1_0(
                data["loggingConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
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
