"""Generated from Smithy shape ``com.amazonaws.sns#AddPermissionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.actions_list
    import aws_sdk_sns.types.delegates_list
    import aws_sdk_sns.types.label
    import aws_sdk_sns.types.topic_arn


class AddPermissionInput(TypedDict):
    topic_arn: "aws_sdk_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic whose access control policy you wish to modify.</p>"""
    label: "aws_sdk_sns.types.label.label"
    """<p>A unique identifier for the new policy statement.</p>"""
    aws_account_id: "aws_sdk_sns.types.delegates_list.DelegatesList"
    """<p>The Amazon Web Services account IDs of the users (principals) who will be given access to the specified actions. The users must have Amazon Web Services account, but do not need to be signed up for this service.</p>"""
    action_name: "aws_sdk_sns.types.actions_list.ActionsList"
    """<p>The action you want to allow for the specified principal(s).</p> <p>Valid values: Any Amazon SNS action name, for example <code>Publish</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddPermissionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))
    pairs.append((f"{prefix}.Label", str(value["label"])))
    import aws_sdk_sns.types.delegates_list

    aws_sdk_sns.types.delegates_list.serialize_query(
        value["aws_account_id"], pairs, f"{prefix}.AWSAccountId"
    )
    import aws_sdk_sns.types.actions_list

    aws_sdk_sns.types.actions_list.serialize_query(
        value["action_name"], pairs, f"{prefix}.ActionName"
    )


def deserialize_query(el: Element) -> AddPermissionInput:
    out: AddPermissionInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("AddPermissionInput.topic_arn required")
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    else:
        raise DeserializationError("AddPermissionInput.label required")
    child_aws_account_id = el.find("AWSAccountId")
    if child_aws_account_id is not None:
        import aws_sdk_sns.types.delegates_list

        out["aws_account_id"] = aws_sdk_sns.types.delegates_list.deserialize_query(
            child_aws_account_id
        )
    else:
        raise DeserializationError("AddPermissionInput.aws_account_id required")
    child_action_name = el.find("ActionName")
    if child_action_name is not None:
        import aws_sdk_sns.types.actions_list

        out["action_name"] = aws_sdk_sns.types.actions_list.deserialize_query(
            child_action_name
        )
    else:
        raise DeserializationError("AddPermissionInput.action_name required")
    return out
