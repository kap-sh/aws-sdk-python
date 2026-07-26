"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.configuration
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.resource_name
    import capo_chime_sdk_identity.types.tag_list


class CreateAppInstanceBotRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code> request.</p>"""
    name: NotRequired["capo_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The user's name.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The request metadata. Limited to a 1KB string in UTF-8.</p>"""
    client_request_token: (
        "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID for the client making the request. Use different tokens for different <code>AppInstanceBots</code>.</p>"""
    tags: NotRequired["capo_chime_sdk_identity.types.tag_list.TagList"]
    """<p>The tags assigned to the <code>AppInstanceBot</code>.</p>"""
    configuration: "capo_chime_sdk_identity.types.configuration.Configuration"
    """<p>Configuration information about the Amazon Lex V2 V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceBotRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["Tags"] = capo_chime_sdk_identity.types.tag_list.serialize_json(
            value["tags"]
        )
    import capo_chime_sdk_identity.types.configuration

    out["Configuration"] = capo_chime_sdk_identity.types.configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> CreateAppInstanceBotRequest:
    out: CreateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
    if "AppInstanceArn" in data:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        raise DeserializationError(
            "CreateAppInstanceBotRequest.app_instance_arn required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "CreateAppInstanceBotRequest.client_request_token required"
        )
    if "Tags" in data:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "Configuration" in data:
        import capo_chime_sdk_identity.types.configuration

        out["configuration"] = (
            capo_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAppInstanceBotRequest.configuration required")
    return out
