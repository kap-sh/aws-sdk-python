"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.client_request_token
    import aws_sdk_chime_sdk_identity.types.configuration
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.resource_name
    import aws_sdk_chime_sdk_identity.types.tag_list


class CreateAppInstanceBotRequest(TypedDict):
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code> request.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The user's name.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The request metadata. Limited to a 1KB string in UTF-8.</p>"""
    client_request_token: (
        "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID for the client making the request. Use different tokens for different <code>AppInstanceBots</code>.</p>"""
    tags: NotRequired["aws_sdk_chime_sdk_identity.types.tag_list.TagList"]
    """<p>The tags assigned to the <code>AppInstanceBot</code>.</p>"""
    configuration: "aws_sdk_chime_sdk_identity.types.configuration.Configuration"
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
        import aws_sdk_chime_sdk_identity.types.tag_list

        out["Tags"] = aws_sdk_chime_sdk_identity.types.tag_list.serialize_json(
            value["tags"]
        )
    import aws_sdk_chime_sdk_identity.types.configuration

    out["Configuration"] = (
        aws_sdk_chime_sdk_identity.types.configuration.serialize_json(
            value["configuration"]
        )
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
        import aws_sdk_chime_sdk_identity.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "Configuration" in data:
        import aws_sdk_chime_sdk_identity.types.configuration

        out["configuration"] = (
            aws_sdk_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAppInstanceBotRequest.configuration required")
    return out
