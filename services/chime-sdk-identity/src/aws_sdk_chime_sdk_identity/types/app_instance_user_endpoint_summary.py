"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.allow_messages
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.endpoint_state
    import aws_sdk_chime_sdk_identity.types.sensitive_string1600
    import aws_sdk_chime_sdk_identity.types.string64


class AppInstanceUserEndpointSummary(TypedDict):
    app_instance_user_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    endpoint_id: NotRequired["aws_sdk_chime_sdk_identity.types.string64.String64"]
    """<p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
    ]
    """<p>The name of the <code>AppInstanceUserEndpoint</code>.</p>"""
    type: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType"
    ]
    """<p>The type of the <code>AppInstanceUserEndpoint</code>.</p>"""
    allow_messages: NotRequired[
        "aws_sdk_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>BBoolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>"""
    endpoint_state: NotRequired[
        "aws_sdk_chime_sdk_identity.types.endpoint_state.EndpointState"
    ]
    """<p>A read-only field that represent the state of an <code>AppInstanceUserEndpoint</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpointSummary) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["Type"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.serialize_json(
                value["type"]
            )
        )
    if "allow_messages" in value:
        import aws_sdk_chime_sdk_identity.types.allow_messages

        out["AllowMessages"] = (
            aws_sdk_chime_sdk_identity.types.allow_messages.serialize_json(
                value["allow_messages"]
            )
        )
    if "endpoint_state" in value:
        import aws_sdk_chime_sdk_identity.types.endpoint_state

        out["EndpointState"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_state.serialize_json(
                value["endpoint_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInstanceUserEndpointSummary:
    out: AppInstanceUserEndpointSummary = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["type"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.deserialize_json(
                data["Type"]
            )
        )
    if "AllowMessages" in data:
        import aws_sdk_chime_sdk_identity.types.allow_messages

        out["allow_messages"] = (
            aws_sdk_chime_sdk_identity.types.allow_messages.deserialize_json(
                data["AllowMessages"]
            )
        )
    if "EndpointState" in data:
        import aws_sdk_chime_sdk_identity.types.endpoint_state

        out["endpoint_state"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_state.deserialize_json(
                data["EndpointState"]
            )
        )
    return out
