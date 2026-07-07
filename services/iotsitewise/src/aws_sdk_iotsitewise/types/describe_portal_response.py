"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.alarms
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.auth_mode
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.email
    import aws_sdk_iotsitewise.types.iam_arn
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.image_location
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.portal_client_id
    import aws_sdk_iotsitewise.types.portal_status
    import aws_sdk_iotsitewise.types.portal_type
    import aws_sdk_iotsitewise.types.portal_type_configuration
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.url


class DescribePortalResponse(TypedDict, closed=True):
    portal_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the portal.</p>"""
    portal_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the portal, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}</code> </p>"""
    portal_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the portal.</p>"""
    portal_description: NotRequired["aws_sdk_iotsitewise.types.description.Description"]
    """<p>The portal's description.</p>"""
    portal_client_id: "aws_sdk_iotsitewise.types.portal_client_id.PortalClientId"
    """<p>The IAM Identity Center application generated client ID (used with IAM Identity Center API operations). IoT SiteWise includes <code>portalClientId</code> for only portals that use IAM Identity Center to authenticate users.</p>"""
    portal_start_url: "aws_sdk_iotsitewise.types.url.Url"
    """<p>The URL for the IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the IoT SiteWise console to get a URL that you can use to access the portal.</p>"""
    portal_contact_email: "aws_sdk_iotsitewise.types.email.Email"
    """<p>The Amazon Web Services administrator's contact email address.</p>"""
    portal_status: "aws_sdk_iotsitewise.types.portal_status.PortalStatus"
    """<p>The current status of the portal, which contains a state and any error message.</p>"""
    portal_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the portal was created, in Unix epoch time.</p>"""
    portal_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the portal was last updated, in Unix epoch time.</p>"""
    portal_logo_image_location: NotRequired[
        "aws_sdk_iotsitewise.types.image_location.ImageLocation"
    ]
    """<p>The portal's logo image, which is available at a URL.</p>"""
    role_arn: NotRequired["aws_sdk_iotsitewise.types.iam_arn.IamArn"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html\">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    portal_auth_mode: NotRequired["aws_sdk_iotsitewise.types.auth_mode.AuthMode"]
    """<p>The service to use to authenticate users to the portal.</p>"""
    notification_sender_email: NotRequired["aws_sdk_iotsitewise.types.email.Email"]
    """<p>The email address that sends alarm notifications.</p>"""
    alarms: NotRequired["aws_sdk_iotsitewise.types.alarms.Alarms"]
    """<p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal.</p>"""
    portal_type: NotRequired["aws_sdk_iotsitewise.types.portal_type.PortalType"]
    """<p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""
    portal_type_configuration: NotRequired[
        "aws_sdk_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
    ]
    """<p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePortalResponse) -> dict:
    out: dict = {}
    out["portalId"] = value["portal_id"]
    out["portalArn"] = value["portal_arn"]
    out["portalName"] = value["portal_name"]
    if "portal_description" in value:
        out["portalDescription"] = value["portal_description"]
    out["portalClientId"] = value["portal_client_id"]
    out["portalStartUrl"] = value["portal_start_url"]
    out["portalContactEmail"] = value["portal_contact_email"]
    import aws_sdk_iotsitewise.types.portal_status

    out["portalStatus"] = aws_sdk_iotsitewise.types.portal_status.serialize_json(
        value["portal_status"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["portalCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["portal_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["portalLastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["portal_last_update_date"]
    )
    if "portal_logo_image_location" in value:
        import aws_sdk_iotsitewise.types.image_location

        out["portalLogoImageLocation"] = (
            aws_sdk_iotsitewise.types.image_location.serialize_json(
                value["portal_logo_image_location"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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


def deserialize_json(data: dict) -> DescribePortalResponse:
    out: DescribePortalResponse = {}  # type: ignore[typeddict-item]
    if "portalId" in data:
        out["portal_id"] = data["portalId"]
    else:
        raise DeserializationError("DescribePortalResponse.portal_id required")
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("DescribePortalResponse.portal_arn required")
    if "portalName" in data:
        out["portal_name"] = data["portalName"]
    else:
        raise DeserializationError("DescribePortalResponse.portal_name required")
    if "portalDescription" in data:
        out["portal_description"] = data["portalDescription"]
    if "portalClientId" in data:
        out["portal_client_id"] = data["portalClientId"]
    else:
        raise DeserializationError("DescribePortalResponse.portal_client_id required")
    if "portalStartUrl" in data:
        out["portal_start_url"] = data["portalStartUrl"]
    else:
        raise DeserializationError("DescribePortalResponse.portal_start_url required")
    if "portalContactEmail" in data:
        out["portal_contact_email"] = data["portalContactEmail"]
    else:
        raise DeserializationError(
            "DescribePortalResponse.portal_contact_email required"
        )
    if "portalStatus" in data:
        import aws_sdk_iotsitewise.types.portal_status

        out["portal_status"] = aws_sdk_iotsitewise.types.portal_status.deserialize_json(
            data["portalStatus"]
        )
    else:
        raise DeserializationError("DescribePortalResponse.portal_status required")
    if "portalCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["portal_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["portalCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePortalResponse.portal_creation_date required"
        )
    if "portalLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["portal_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["portalLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePortalResponse.portal_last_update_date required"
        )
    if "portalLogoImageLocation" in data:
        import aws_sdk_iotsitewise.types.image_location

        out["portal_logo_image_location"] = (
            aws_sdk_iotsitewise.types.image_location.deserialize_json(
                data["portalLogoImageLocation"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
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
