"""Generated from Smithy shape ``com.amazonaws.connect#AuthenticationProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.access_token_duration
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.authentication_profile_description
    import aws_sdk_connect.types.authentication_profile_id
    import aws_sdk_connect.types.authentication_profile_name
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.inactivity_duration
    import aws_sdk_connect.types.ip_cidr_list
    import aws_sdk_connect.types.refresh_token_duration
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class AuthenticationProfile(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.authentication_profile_id.AuthenticationProfileId"
    ]
    """<p>A unique identifier for the authentication profile. </p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the authentication profile.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.authentication_profile_name.AuthenticationProfileName"
    ]
    """<p>The name for the authentication profile.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.authentication_profile_description.AuthenticationProfileDescription"
    ]
    """<p>The description for the authentication profile.</p>"""
    allowed_ips: NotRequired["aws_sdk_connect.types.ip_cidr_list.IpCidrList"]
    r"""<p>A list of IP address range strings that are allowed to access the Connect Customer instance. For more information about how to configure IP addresses, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac\">Configure IP address based access control</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    blocked_ips: NotRequired["aws_sdk_connect.types.ip_cidr_list.IpCidrList"]
    r"""<p>A list of IP address range strings that are blocked from accessing the Connect Customer instance. For more information about how to configure IP addresses, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac\">Configure IP address based access control</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    is_default: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Shows whether the authentication profile is the default authentication profile for the Connect Customer instance. The default authentication profile applies to all agents in an Connect Customer instance, unless overridden by another authentication profile.</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the authentication profile was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the authentication profile was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the authentication profile was last modified.</p>"""
    periodic_session_duration: NotRequired[
        "aws_sdk_connect.types.access_token_duration.AccessTokenDuration"
    ]
    r"""<p>The short lived session duration configuration for users logged in to Connect Customer, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts\">Configure the session duration</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    max_session_duration: NotRequired[
        "aws_sdk_connect.types.refresh_token_duration.RefreshTokenDuration"
    ]
    r"""<p>The long lived session duration for users logged in to Connect Customer, in minutes. After this time period, users must log in again. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts\">Configure the session duration</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    session_inactivity_duration: NotRequired[
        "aws_sdk_connect.types.inactivity_duration.InactivityDuration"
    ]
    """<p>The period, in minutes, before an agent is automatically signed out of the contact center when they go inactive.</p>"""
    session_inactivity_handling_enabled: NotRequired[
        "aws_sdk_connect.types.boolean.Boolean"
    ]
    """<p>Determines if automatic logout on user inactivity is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProfile) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "allowed_ips" in value:
        import aws_sdk_connect.types.ip_cidr_list

        out["AllowedIps"] = aws_sdk_connect.types.ip_cidr_list.serialize_json(
            value["allowed_ips"]
        )
    if "blocked_ips" in value:
        import aws_sdk_connect.types.ip_cidr_list

        out["BlockedIps"] = aws_sdk_connect.types.ip_cidr_list.serialize_json(
            value["blocked_ips"]
        )
    out["IsDefault"] = value.get("is_default", False)
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "periodic_session_duration" in value:
        out["PeriodicSessionDuration"] = value["periodic_session_duration"]
    if "max_session_duration" in value:
        out["MaxSessionDuration"] = value["max_session_duration"]
    if "session_inactivity_duration" in value:
        out["SessionInactivityDuration"] = value["session_inactivity_duration"]
    if "session_inactivity_handling_enabled" in value:
        out["SessionInactivityHandlingEnabled"] = value[
            "session_inactivity_handling_enabled"
        ]
    return out


def deserialize_json(data: dict) -> AuthenticationProfile:
    out: AuthenticationProfile = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AllowedIps" in data:
        import aws_sdk_connect.types.ip_cidr_list

        out["allowed_ips"] = aws_sdk_connect.types.ip_cidr_list.deserialize_json(
            data["AllowedIps"]
        )
    if "BlockedIps" in data:
        import aws_sdk_connect.types.ip_cidr_list

        out["blocked_ips"] = aws_sdk_connect.types.ip_cidr_list.deserialize_json(
            data["BlockedIps"]
        )
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "PeriodicSessionDuration" in data:
        out["periodic_session_duration"] = data["PeriodicSessionDuration"]
    if "MaxSessionDuration" in data:
        out["max_session_duration"] = data["MaxSessionDuration"]
    if "SessionInactivityDuration" in data:
        out["session_inactivity_duration"] = data["SessionInactivityDuration"]
    if "SessionInactivityHandlingEnabled" in data:
        out["session_inactivity_handling_enabled"] = data[
            "SessionInactivityHandlingEnabled"
        ]
    return out
