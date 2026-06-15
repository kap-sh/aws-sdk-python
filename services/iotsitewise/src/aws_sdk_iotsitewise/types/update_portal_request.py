"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdatePortalRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.alarms
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.email
    import aws_sdk_iotsitewise.types.iam_arn
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.image
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.portal_type
    import aws_sdk_iotsitewise.types.portal_type_configuration


class UpdatePortalRequest(TypedDict):
    portal_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the portal to update.</p>"""
    portal_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A new friendly name for the portal.</p>"""
    portal_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A new description for the portal.</p>"""
    portal_contact_email: "aws_sdk_iotsitewise.types.email.Email"
    """<p>The Amazon Web Services administrator's contact email address.</p>"""
    portal_logo_image: NotRequired["aws_sdk_iotsitewise.types.image.Image"]
    role_arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    notification_sender_email: NotRequired["aws_sdk_iotsitewise.types.email.Email"]
    """<p>The email address that sends alarm notifications.</p>"""
    alarms: NotRequired["aws_sdk_iotsitewise.types.alarms.Alarms"]
    r"""<p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html\">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>"""
    portal_type: NotRequired["aws_sdk_iotsitewise.types.portal_type.PortalType"]
    """<p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""
    portal_type_configuration: NotRequired[
        "aws_sdk_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
    ]
    """<p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalRequest) -> dict:
    out: dict = {}
    out["portalName"] = value["portal_name"]
    if "portal_description" in value:
        out["portalDescription"] = value["portal_description"]
    out["portalContactEmail"] = value["portal_contact_email"]
    if "portal_logo_image" in value:
        import aws_sdk_iotsitewise.types.image

        out["portalLogoImage"] = aws_sdk_iotsitewise.types.image.serialize_json(
            value["portal_logo_image"]
        )
    out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "notification_sender_email" in value:
        out["notificationSenderEmail"] = value["notification_sender_email"]
    if "alarms" in value:
        import aws_sdk_iotsitewise.types.alarms

        out["alarms"] = aws_sdk_iotsitewise.types.alarms.serialize_json(value["alarms"])
    if "portal_type" in value:
        import aws_sdk_iotsitewise.types.portal_type

        out["portalType"] = aws_sdk_iotsitewise.types.portal_type.serialize_json(
            value["portal_type"]
        )
    if "portal_type_configuration" in value:
        import aws_sdk_iotsitewise.types.portal_type_configuration

        out["portalTypeConfiguration"] = (
            aws_sdk_iotsitewise.types.portal_type_configuration.serialize_json(
                value["portal_type_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePortalRequest:
    out: UpdatePortalRequest = {}  # type: ignore[typeddict-item]
    if "portalName" in data:
        out["portal_name"] = data["portalName"]
    else:
        raise DeserializationError("UpdatePortalRequest.portal_name required")
    if "portalDescription" in data:
        out["portal_description"] = data["portalDescription"]
    if "portalContactEmail" in data:
        out["portal_contact_email"] = data["portalContactEmail"]
    else:
        raise DeserializationError("UpdatePortalRequest.portal_contact_email required")
    if "portalLogoImage" in data:
        import aws_sdk_iotsitewise.types.image

        out["portal_logo_image"] = aws_sdk_iotsitewise.types.image.deserialize_json(
            data["portalLogoImage"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdatePortalRequest.role_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "notificationSenderEmail" in data:
        out["notification_sender_email"] = data["notificationSenderEmail"]
    if "alarms" in data:
        import aws_sdk_iotsitewise.types.alarms

        out["alarms"] = aws_sdk_iotsitewise.types.alarms.deserialize_json(
            data["alarms"]
        )
    if "portalType" in data:
        import aws_sdk_iotsitewise.types.portal_type

        out["portal_type"] = aws_sdk_iotsitewise.types.portal_type.deserialize_json(
            data["portalType"]
        )
    if "portalTypeConfiguration" in data:
        import aws_sdk_iotsitewise.types.portal_type_configuration

        out["portal_type_configuration"] = (
            aws_sdk_iotsitewise.types.portal_type_configuration.deserialize_json(
                data["portalTypeConfiguration"]
            )
        )
    return out
