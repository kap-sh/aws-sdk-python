"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type
    import aws_sdk_secrets_manager.types.tag_list_type


class TagResourceRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    r"""<p>The identifier for the secret to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen\">Finding a secret from a partial ARN</a>.</p>"""
    tags: "aws_sdk_secrets_manager.types.tag_list_type.TagListType"
    r"""<p>The tags to attach to the secret as a JSON text string argument. Each element in the list consists of a <code>Key</code> and a <code>Value</code>.</p> <p>For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html\">Specifying parameter values for the Amazon Web Services CLI</a> in the Amazon Web Services CLI User Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    import aws_sdk_secrets_manager.types.tag_list_type

    out["Tags"] = aws_sdk_secrets_manager.types.tag_list_type.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("TagResourceRequest.secret_id required")
    if "Tags" in data:
        import aws_sdk_secrets_manager.types.tag_list_type

        out["tags"] = (
            aws_sdk_secrets_manager.types.tag_list_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
