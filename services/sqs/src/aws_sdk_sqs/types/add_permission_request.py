"""Generated from Smithy shape ``com.amazonaws.sqs#AddPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.action_name_list
    import aws_sdk_sqs.types.aws_account_id_list
    import aws_sdk_sqs.types.string


class AddPermissionRequest(TypedDict):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue to which permissions are added.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    label: "aws_sdk_sqs.types.string.String"
    """<p>The unique identification of the permission you're setting (for example, <code>AliceSendMessage</code>). Maximum 80 characters. Allowed characters include alphanumeric characters, hyphens (<code>-</code>), and underscores (<code>_</code>).</p>"""
    aws_account_ids: "aws_sdk_sqs.types.aws_account_id_list.AWSAccountIdList"
    r"""<p>The Amazon Web Services account numbers of the <a href=\"https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P\">principals</a> who are to receive permission. For information about locating the Amazon Web Services account identification, see <a href=\"https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html#sqs-api-request-authentication\">Your Amazon Web Services Identifiers</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""
    actions: "aws_sdk_sqs.types.action_name_list.ActionNameList"
    r"""<p>The action the client wants to allow for the specified principal. Valid values: the name of any action or <code>*</code>.</p> <p>For more information about these actions, see <a href=\"https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html\">Overview of Managing Access Permissions to Your Amazon Simple Queue Service Resource</a> in the <i>Amazon SQS Developer Guide</i>.</p> <p>Specifying <code>SendMessage</code>, <code>DeleteMessage</code>, or <code>ChangeMessageVisibility</code> for <code>ActionName.n</code> also grants permissions for the corresponding batch versions of those actions: <code>SendMessageBatch</code>, <code>DeleteMessageBatch</code>, and <code>ChangeMessageVisibilityBatch</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddPermissionRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["Label"] = value["label"]
    import aws_sdk_sqs.types.aws_account_id_list

    out["AWSAccountIds"] = aws_sdk_sqs.types.aws_account_id_list.serialize_aws_json_1_0(
        value["aws_account_ids"]
    )
    import aws_sdk_sqs.types.action_name_list

    out["Actions"] = aws_sdk_sqs.types.action_name_list.serialize_aws_json_1_0(
        value["actions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddPermissionRequest:
    out: AddPermissionRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("AddPermissionRequest.queue_url required")
    if "Label" in data:
        out["label"] = data["Label"]
    else:
        raise DeserializationError("AddPermissionRequest.label required")
    if "AWSAccountIds" in data:
        import aws_sdk_sqs.types.aws_account_id_list

        out["aws_account_ids"] = (
            aws_sdk_sqs.types.aws_account_id_list.deserialize_aws_json_1_0(
                data["AWSAccountIds"]
            )
        )
    else:
        raise DeserializationError("AddPermissionRequest.aws_account_ids required")
    if "Actions" in data:
        import aws_sdk_sqs.types.action_name_list

        out["actions"] = aws_sdk_sqs.types.action_name_list.deserialize_aws_json_1_0(
            data["Actions"]
        )
    else:
        raise DeserializationError("AddPermissionRequest.actions required")
    return out
