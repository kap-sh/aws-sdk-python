"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.client_request_token
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.processor_list
    import capo_chime_sdk_messaging.types.tag_list


class CreateChannelFlowRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow request.</p>"""
    processors: "capo_chime_sdk_messaging.types.processor_list.ProcessorList"
    """<p>Information about the processor Lambda functions.</p>"""
    name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name of the channel flow.</p>"""
    tags: NotRequired["capo_chime_sdk_messaging.types.tag_list.TagList"]
    """<p>The tags for the creation request.</p>"""
    client_request_token: (
        "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The client token for the request. An Idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelFlowRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    import capo_chime_sdk_messaging.types.processor_list

    out["Processors"] = capo_chime_sdk_messaging.types.processor_list.serialize_json(
        value["processors"]
    )
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_chime_sdk_messaging.types.tag_list

        out["Tags"] = capo_chime_sdk_messaging.types.tag_list.serialize_json(
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
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.deserialize_json(
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
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "CreateChannelFlowRequest.client_request_token required"
        )
    return out
