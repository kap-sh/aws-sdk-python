"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.add_header_action
    import aws_sdk_mailmanager.types.archive_action
    import aws_sdk_mailmanager.types.bounce_action
    import aws_sdk_mailmanager.types.deliver_to_mailbox_action
    import aws_sdk_mailmanager.types.deliver_to_q_business_action
    import aws_sdk_mailmanager.types.drop_action
    import aws_sdk_mailmanager.types.invoke_lambda_action
    import aws_sdk_mailmanager.types.relay_action
    import aws_sdk_mailmanager.types.replace_recipient_action
    import aws_sdk_mailmanager.types.s3_action
    import aws_sdk_mailmanager.types.send_action
    import aws_sdk_mailmanager.types.sns_action


class _RuleAction_Drop(TypedDict, closed=True):
    Drop: "aws_sdk_mailmanager.types.drop_action.DropAction"


class _RuleAction_Relay(TypedDict, closed=True):
    Relay: "aws_sdk_mailmanager.types.relay_action.RelayAction"


class _RuleAction_Archive(TypedDict, closed=True):
    Archive: "aws_sdk_mailmanager.types.archive_action.ArchiveAction"


class _RuleAction_WriteToS3(TypedDict, closed=True):
    WriteToS3: "aws_sdk_mailmanager.types.s3_action.S3Action"


class _RuleAction_Send(TypedDict, closed=True):
    Send: "aws_sdk_mailmanager.types.send_action.SendAction"


class _RuleAction_AddHeader(TypedDict, closed=True):
    AddHeader: "aws_sdk_mailmanager.types.add_header_action.AddHeaderAction"


class _RuleAction_ReplaceRecipient(TypedDict, closed=True):
    ReplaceRecipient: (
        "aws_sdk_mailmanager.types.replace_recipient_action.ReplaceRecipientAction"
    )


class _RuleAction_DeliverToMailbox(TypedDict, closed=True):
    DeliverToMailbox: (
        "aws_sdk_mailmanager.types.deliver_to_mailbox_action.DeliverToMailboxAction"
    )


class _RuleAction_DeliverToQBusiness(TypedDict, closed=True):
    DeliverToQBusiness: "aws_sdk_mailmanager.types.deliver_to_q_business_action.DeliverToQBusinessAction"


class _RuleAction_PublishToSns(TypedDict, closed=True):
    PublishToSns: "aws_sdk_mailmanager.types.sns_action.SnsAction"


class _RuleAction_Bounce(TypedDict, closed=True):
    Bounce: "aws_sdk_mailmanager.types.bounce_action.BounceAction"


class _RuleAction_InvokeLambda(TypedDict, closed=True):
    InvokeLambda: "aws_sdk_mailmanager.types.invoke_lambda_action.InvokeLambdaAction"


RuleAction: TypeAlias = (
    _RuleAction_Drop
    | _RuleAction_Relay
    | _RuleAction_Archive
    | _RuleAction_WriteToS3
    | _RuleAction_Send
    | _RuleAction_AddHeader
    | _RuleAction_ReplaceRecipient
    | _RuleAction_DeliverToMailbox
    | _RuleAction_DeliverToQBusiness
    | _RuleAction_PublishToSns
    | _RuleAction_Bounce
    | _RuleAction_InvokeLambda
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleAction) -> dict:
    if "Drop" in value:
        import aws_sdk_mailmanager.types.drop_action

        return {
            "Drop": aws_sdk_mailmanager.types.drop_action.serialize_aws_json_1_0(
                value["Drop"]
            )
        }
    elif "Relay" in value:
        import aws_sdk_mailmanager.types.relay_action

        return {
            "Relay": aws_sdk_mailmanager.types.relay_action.serialize_aws_json_1_0(
                value["Relay"]
            )
        }
    elif "Archive" in value:
        import aws_sdk_mailmanager.types.archive_action

        return {
            "Archive": aws_sdk_mailmanager.types.archive_action.serialize_aws_json_1_0(
                value["Archive"]
            )
        }
    elif "WriteToS3" in value:
        import aws_sdk_mailmanager.types.s3_action

        return {
            "WriteToS3": aws_sdk_mailmanager.types.s3_action.serialize_aws_json_1_0(
                value["WriteToS3"]
            )
        }
    elif "Send" in value:
        import aws_sdk_mailmanager.types.send_action

        return {
            "Send": aws_sdk_mailmanager.types.send_action.serialize_aws_json_1_0(
                value["Send"]
            )
        }
    elif "AddHeader" in value:
        import aws_sdk_mailmanager.types.add_header_action

        return {
            "AddHeader": aws_sdk_mailmanager.types.add_header_action.serialize_aws_json_1_0(
                value["AddHeader"]
            )
        }
    elif "ReplaceRecipient" in value:
        import aws_sdk_mailmanager.types.replace_recipient_action

        return {
            "ReplaceRecipient": aws_sdk_mailmanager.types.replace_recipient_action.serialize_aws_json_1_0(
                value["ReplaceRecipient"]
            )
        }
    elif "DeliverToMailbox" in value:
        import aws_sdk_mailmanager.types.deliver_to_mailbox_action

        return {
            "DeliverToMailbox": aws_sdk_mailmanager.types.deliver_to_mailbox_action.serialize_aws_json_1_0(
                value["DeliverToMailbox"]
            )
        }
    elif "DeliverToQBusiness" in value:
        import aws_sdk_mailmanager.types.deliver_to_q_business_action

        return {
            "DeliverToQBusiness": aws_sdk_mailmanager.types.deliver_to_q_business_action.serialize_aws_json_1_0(
                value["DeliverToQBusiness"]
            )
        }
    elif "PublishToSns" in value:
        import aws_sdk_mailmanager.types.sns_action

        return {
            "PublishToSns": aws_sdk_mailmanager.types.sns_action.serialize_aws_json_1_0(
                value["PublishToSns"]
            )
        }
    elif "Bounce" in value:
        import aws_sdk_mailmanager.types.bounce_action

        return {
            "Bounce": aws_sdk_mailmanager.types.bounce_action.serialize_aws_json_1_0(
                value["Bounce"]
            )
        }
    elif "InvokeLambda" in value:
        import aws_sdk_mailmanager.types.invoke_lambda_action

        return {
            "InvokeLambda": aws_sdk_mailmanager.types.invoke_lambda_action.serialize_aws_json_1_0(
                value["InvokeLambda"]
            )
        }
    else:
        raise SerializationError("RuleAction: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleAction:
    if "Drop" in data:
        import aws_sdk_mailmanager.types.drop_action

        return {
            "Drop": aws_sdk_mailmanager.types.drop_action.deserialize_aws_json_1_0(
                data["Drop"]
            )
        }
    elif "Relay" in data:
        import aws_sdk_mailmanager.types.relay_action

        return {
            "Relay": aws_sdk_mailmanager.types.relay_action.deserialize_aws_json_1_0(
                data["Relay"]
            )
        }
    elif "Archive" in data:
        import aws_sdk_mailmanager.types.archive_action

        return {
            "Archive": aws_sdk_mailmanager.types.archive_action.deserialize_aws_json_1_0(
                data["Archive"]
            )
        }
    elif "WriteToS3" in data:
        import aws_sdk_mailmanager.types.s3_action

        return {
            "WriteToS3": aws_sdk_mailmanager.types.s3_action.deserialize_aws_json_1_0(
                data["WriteToS3"]
            )
        }
    elif "Send" in data:
        import aws_sdk_mailmanager.types.send_action

        return {
            "Send": aws_sdk_mailmanager.types.send_action.deserialize_aws_json_1_0(
                data["Send"]
            )
        }
    elif "AddHeader" in data:
        import aws_sdk_mailmanager.types.add_header_action

        return {
            "AddHeader": aws_sdk_mailmanager.types.add_header_action.deserialize_aws_json_1_0(
                data["AddHeader"]
            )
        }
    elif "ReplaceRecipient" in data:
        import aws_sdk_mailmanager.types.replace_recipient_action

        return {
            "ReplaceRecipient": aws_sdk_mailmanager.types.replace_recipient_action.deserialize_aws_json_1_0(
                data["ReplaceRecipient"]
            )
        }
    elif "DeliverToMailbox" in data:
        import aws_sdk_mailmanager.types.deliver_to_mailbox_action

        return {
            "DeliverToMailbox": aws_sdk_mailmanager.types.deliver_to_mailbox_action.deserialize_aws_json_1_0(
                data["DeliverToMailbox"]
            )
        }
    elif "DeliverToQBusiness" in data:
        import aws_sdk_mailmanager.types.deliver_to_q_business_action

        return {
            "DeliverToQBusiness": aws_sdk_mailmanager.types.deliver_to_q_business_action.deserialize_aws_json_1_0(
                data["DeliverToQBusiness"]
            )
        }
    elif "PublishToSns" in data:
        import aws_sdk_mailmanager.types.sns_action

        return {
            "PublishToSns": aws_sdk_mailmanager.types.sns_action.deserialize_aws_json_1_0(
                data["PublishToSns"]
            )
        }
    elif "Bounce" in data:
        import aws_sdk_mailmanager.types.bounce_action

        return {
            "Bounce": aws_sdk_mailmanager.types.bounce_action.deserialize_aws_json_1_0(
                data["Bounce"]
            )
        }
    elif "InvokeLambda" in data:
        import aws_sdk_mailmanager.types.invoke_lambda_action

        return {
            "InvokeLambda": aws_sdk_mailmanager.types.invoke_lambda_action.deserialize_aws_json_1_0(
                data["InvokeLambda"]
            )
        }
    else:
        raise DeserializationError("RuleAction: no recognized variant key")
