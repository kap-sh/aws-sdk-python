"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.client_request_token
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.processor_list
    import aws_sdk_chime_sdk_messaging.types.tag_list


class CreateChannelFlowRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow request.</p>"""
    processors: "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList"
    """<p>Information about the processor Lambda functions.</p>"""
    name: (
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    )
    """<p>The name of the channel flow.</p>"""
    tags: NotRequired["aws_sdk_chime_sdk_messaging.types.tag_list.TagList"]
    """<p>The tags for the creation request.</p>"""
    client_request_token: (
        "aws_sdk_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The client token for the request. An Idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelFlowRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    import aws_sdk_chime_sdk_messaging.types.processor_list

    out["Processors"] = aws_sdk_chime_sdk_messaging.types.processor_list.serialize_json(
        value["processors"]
    )
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_chime_sdk_messaging.types.tag_list

        out["Tags"] = aws_sdk_chime_sdk_messaging.types.tag_list.serialize_json(
            value["tags"]
        )
    out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateChannelFlowRequest:
    out: CreateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        raise DeserializationError("CreateChannelFlowRequest.app_instance_arn required")
    if "Processors" in data:
        import aws_sdk_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            aws_sdk_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    else:
        raise DeserializationError("CreateChannelFlowRequest.processors required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateChannelFlowRequest.name required")
    if "Tags" in data:
        import aws_sdk_chime_sdk_messaging.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_messaging.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "CreateChannelFlowRequest.client_request_token required"
        )
    return out
