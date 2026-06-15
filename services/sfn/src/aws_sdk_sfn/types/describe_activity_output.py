"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeActivityOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.encryption_configuration
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.timestamp


class DescribeActivityOutput(TypedDict):
    activity_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the activity.</p>"""
    name: "aws_sdk_sfn.types.name.Name"
    r"""<p>The name of the activity.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the activity is created.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings for configured server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeActivityOutput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    out["name"] = value["name"]
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "encryption_configuration" in value:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeActivityOutput:
    out: DescribeActivityOutput = {}  # type: ignore[typeddict-item]
    if "activityArn" in data:
        out["activity_arn"] = data["activityArn"]
    else:
        raise DeserializationError("DescribeActivityOutput.activity_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DescribeActivityOutput.name required")
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DescribeActivityOutput.creation_date required")
    if "encryptionConfiguration" in data:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
