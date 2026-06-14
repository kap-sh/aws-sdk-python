"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreatePortalRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.alarms
    import aws_sdk_iotsitewise.types.auth_mode
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.email
    import aws_sdk_iotsitewise.types.iam_arn
    import aws_sdk_iotsitewise.types.image_file
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.portal_type
    import aws_sdk_iotsitewise.types.portal_type_configuration
    import aws_sdk_iotsitewise.types.tag_map


class CreatePortalRequest(TypedDict):
    portal_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>A friendly name for the portal.</p>"""
    portal_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>A description for the portal.</p>"""
    portal_contact_email: "aws_sdk_iotsitewise.types.email.Email"
    """<p>The Amazon Web Services administrator's contact email address.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    portal_logo_image_file: NotRequired[
        "aws_sdk_iotsitewise.types.image_file.ImageFile"
    ]
    """<p>A logo image to display in the portal. Upload a square, high-resolution image. The image is displayed on a dark background.</p>"""
    role_arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_iotsitewise.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the portal. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html\">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    portal_auth_mode: NotRequired["aws_sdk_iotsitewise.types.auth_mode.AuthMode"]
    r"""<p>The service to use to authenticate users to the portal. Choose from the following options:</p> <ul> <li> <p> <code>SSO</code> – The portal uses IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso\">Enabling IAM Identity Center</a> in the <i>IoT SiteWise User Guide</i>. This option is only available in Amazon Web Services Regions other than the China Regions.</p> </li> <li> <p> <code>IAM</code> – The portal uses Identity and Access Management to authenticate users and manage user permissions.</p> </li> </ul> <p>You can't change this value after you create a portal.</p> <p>Default: <code>SSO</code> </p>"""
    notification_sender_email: NotRequired["aws_sdk_iotsitewise.types.email.Email"]
    r"""<p>The email address that sends alarm notifications.</p> <important> <p>If you use the <a href=\"https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html\">IoT Events managed Lambda function</a> to manage your emails, you must <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html\">verify the sender email address in Amazon SES</a>.</p> </important>"""
    alarms: NotRequired["aws_sdk_iotsitewise.types.alarms.Alarms"]
    r"""<p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html\">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>"""
    portal_type: NotRequired["aws_sdk_iotsitewise.types.portal_type.PortalType"]
    """<p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""
    portal_type_configuration: NotRequired[
        "aws_sdk_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
    ]
    """<p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalRequest) -> dict:
    out: dict = {}
    out["portalName"] = value["portal_name"]
    if "portal_description" in value:
        out["portalDescription"] = value["portal_description"]
    out["portalContactEmail"] = value["portal_contact_email"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "portal_logo_image_file" in value:
        import aws_sdk_iotsitewise.types.image_file

        out["portalLogoImageFile"] = (
            aws_sdk_iotsitewise.types.image_file.serialize_json(
                value["portal_logo_image_file"]
            )
        )
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.serialize_json(value["tags"])
    if "portal_auth_mode" in value:
        import aws_sdk_iotsitewise.types.auth_mode

        out["portalAuthMode"] = aws_sdk_iotsitewise.types.auth_mode.serialize_json(
            value["portal_auth_mode"]
        )
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


def deserialize_json(data: dict) -> CreatePortalRequest:
    out: CreatePortalRequest = {}  # type: ignore[typeddict-item]
    if "portalName" in data:
        out["portal_name"] = data["portalName"]
    else:
        raise DeserializationError("CreatePortalRequest.portal_name required")
    if "portalDescription" in data:
        out["portal_description"] = data["portalDescription"]
    if "portalContactEmail" in data:
        out["portal_contact_email"] = data["portalContactEmail"]
    else:
        raise DeserializationError("CreatePortalRequest.portal_contact_email required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "portalLogoImageFile" in data:
        import aws_sdk_iotsitewise.types.image_file

        out["portal_logo_image_file"] = (
            aws_sdk_iotsitewise.types.image_file.deserialize_json(
                data["portalLogoImageFile"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreatePortalRequest.role_arn required")
    if "tags" in data:
        import aws_sdk_iotsitewise.types.tag_map

        out["tags"] = aws_sdk_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    if "portalAuthMode" in data:
        import aws_sdk_iotsitewise.types.auth_mode

        out["portal_auth_mode"] = aws_sdk_iotsitewise.types.auth_mode.deserialize_json(
            data["portalAuthMode"]
        )
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
