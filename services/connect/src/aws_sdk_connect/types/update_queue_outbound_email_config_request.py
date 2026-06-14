"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueOutboundEmailConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.outbound_email_config
    import aws_sdk_connect.types.queue_id


class UpdateQueueOutboundEmailConfigRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    outbound_email_config: (
        "aws_sdk_connect.types.outbound_email_config.OutboundEmailConfig"
    )
    """<p>The outbound email address ID for a specified queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueOutboundEmailConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.outbound_email_config

    out["OutboundEmailConfig"] = (
        aws_sdk_connect.types.outbound_email_config.serialize_json(
            value["outbound_email_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueOutboundEmailConfigRequest:
    out: UpdateQueueOutboundEmailConfigRequest = {}  # type: ignore[typeddict-item]
    if "OutboundEmailConfig" in data:
        import aws_sdk_connect.types.outbound_email_config

        out["outbound_email_config"] = (
            aws_sdk_connect.types.outbound_email_config.deserialize_json(
                data["OutboundEmailConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQueueOutboundEmailConfigRequest.outbound_email_config required"
        )
    return out
