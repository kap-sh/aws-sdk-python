"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#RegisterAppInstanceUserEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.allow_messages
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.client_request_token
    import aws_sdk_chime_sdk_identity.types.endpoint_attributes
    import aws_sdk_chime_sdk_identity.types.sensitive_chime_arn
    import aws_sdk_chime_sdk_identity.types.sensitive_string1600


class RegisterAppInstanceUserEndpointRequest(TypedDict):
    app_instance_user_arn: (
        "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn"
    )
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
    ]
    """<p>The name of the <code>AppInstanceUserEndpoint</code>.</p>"""
    type: "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType"
    """<p>The type of the <code>AppInstanceUserEndpoint</code>. Supported types:</p> <ul> <li> <p> <code>APNS</code>: The mobile notification service for an Apple device.</p> </li> <li> <p> <code>APNS_SANDBOX</code>: The sandbox environment of the mobile notification service for an Apple device.</p> </li> <li> <p> <code>GCM</code>: The mobile notification service for an Android device.</p> </li> </ul> <p>Populate the <code>ResourceArn</code> value of each type as <code>PinpointAppArn</code>.</p>"""
    resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the resource to which the endpoint belongs.</p>"""
    endpoint_attributes: (
        "aws_sdk_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes"
    )
    """<p>The attributes of an <code>Endpoint</code>.</p>"""
    client_request_token: (
        "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID assigned to the request. Use different tokens to register other endpoints.</p>"""
    allow_messages: NotRequired[
        "aws_sdk_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. <code>ALL</code> indicates the endpoint receives all messages. <code>NONE</code> indicates the endpoint receives no messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAppInstanceUserEndpointRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type

    out["Type"] = (
        aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.serialize_json(
            value["type"]
        )
    )
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_chime_sdk_identity.types.endpoint_attributes

    out["EndpointAttributes"] = (
        aws_sdk_chime_sdk_identity.types.endpoint_attributes.serialize_json(
            value["endpoint_attributes"]
        )
    )
    out["ClientRequestToken"] = value["client_request_token"]
    if "allow_messages" in value:
        import aws_sdk_chime_sdk_identity.types.allow_messages

        out["AllowMessages"] = (
            aws_sdk_chime_sdk_identity.types.allow_messages.serialize_json(
                value["allow_messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterAppInstanceUserEndpointRequest:
    out: RegisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["type"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterAppInstanceUserEndpointRequest.type required"
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "RegisterAppInstanceUserEndpointRequest.resource_arn required"
        )
    if "EndpointAttributes" in data:
        import aws_sdk_chime_sdk_identity.types.endpoint_attributes

        out["endpoint_attributes"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_attributes.deserialize_json(
                data["EndpointAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterAppInstanceUserEndpointRequest.endpoint_attributes required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "RegisterAppInstanceUserEndpointRequest.client_request_token required"
        )
    if "AllowMessages" in data:
        import aws_sdk_chime_sdk_identity.types.allow_messages

        out["allow_messages"] = (
            aws_sdk_chime_sdk_identity.types.allow_messages.deserialize_json(
                data["AllowMessages"]
            )
        )
    return out
