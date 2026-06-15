"""Generated from Smithy shape ``com.amazonaws.connect#CreatePushNotificationRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_configuration
    import aws_sdk_connect.types.device_token
    import aws_sdk_connect.types.device_type
    import aws_sdk_connect.types.instance_id


class CreatePushNotificationRegistrationRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    pinpoint_app_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the Pinpoint application.</p>"""
    device_token: "aws_sdk_connect.types.device_token.DeviceToken"
    """<p>The push notification token issued by the Apple or Google gateways.</p>"""
    device_type: "aws_sdk_connect.types.device_type.DeviceType"
    """<p>The device type to use when sending the message.</p>"""
    contact_configuration: (
        "aws_sdk_connect.types.contact_configuration.ContactConfiguration"
    )
    """<p>The contact configuration for push notification registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushNotificationRegistrationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["PinpointAppArn"] = value["pinpoint_app_arn"]
    out["DeviceToken"] = value["device_token"]
    import aws_sdk_connect.types.device_type

    out["DeviceType"] = aws_sdk_connect.types.device_type.serialize_json(
        value["device_type"]
    )
    import aws_sdk_connect.types.contact_configuration

    out["ContactConfiguration"] = (
        aws_sdk_connect.types.contact_configuration.serialize_json(
            value["contact_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePushNotificationRegistrationRequest:
    out: CreatePushNotificationRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "PinpointAppArn" in data:
        out["pinpoint_app_arn"] = data["PinpointAppArn"]
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.pinpoint_app_arn required"
        )
    if "DeviceToken" in data:
        out["device_token"] = data["DeviceToken"]
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.device_token required"
        )
    if "DeviceType" in data:
        import aws_sdk_connect.types.device_type

        out["device_type"] = aws_sdk_connect.types.device_type.deserialize_json(
            data["DeviceType"]
        )
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.device_type required"
        )
    if "ContactConfiguration" in data:
        import aws_sdk_connect.types.contact_configuration

        out["contact_configuration"] = (
            aws_sdk_connect.types.contact_configuration.deserialize_json(
                data["ContactConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.contact_configuration required"
        )
    return out
