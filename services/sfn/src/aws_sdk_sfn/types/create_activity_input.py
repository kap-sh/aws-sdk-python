"""Generated from Smithy shape ``com.amazonaws.sfn#CreateActivityInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.encryption_configuration
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.tag_list


class CreateActivityInput(TypedDict):
    name: "aws_sdk_sfn.types.name.Name"
    r"""<p>The name of the activity to create. This name must be unique for your Amazon Web Services account and region for 90 days. For more information, see <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/limits.html#service-limits-state-machine-executions\"> Limits Related to State Machine Executions</a> in the <i>Step Functions Developer Guide</i>.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>\" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    tags: NotRequired["aws_sdk_sfn.types.tag_list.TagList"]
    r"""<p>The list of tags to add to a resource.</p> <p>An array of key-value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html\">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateActivityInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "encryption_configuration" in value:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateActivityInput:
    out: CreateActivityInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateActivityInput.name required")
    if "tags" in data:
        import aws_sdk_sfn.types.tag_list

        out["tags"] = aws_sdk_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if "encryptionConfiguration" in data:
        import aws_sdk_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
