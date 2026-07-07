"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAuthenticationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.access_token_duration
    import aws_sdk_connect.types.authentication_profile_description
    import aws_sdk_connect.types.authentication_profile_id
    import aws_sdk_connect.types.authentication_profile_name
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.inactivity_duration
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.ip_cidr_list


class UpdateAuthenticationProfileRequest(TypedDict, closed=True):
    authentication_profile_id: (
        "aws_sdk_connect.types.authentication_profile_id.AuthenticationProfileId"
    )
    """<p>A unique identifier for the authentication profile. </p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.authentication_profile_name.AuthenticationProfileName"
    ]
    """<p>The name for the authentication profile.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.authentication_profile_description.AuthenticationProfileDescription"
    ]
    """<p>The description for the authentication profile.</p>"""
    allowed_ips: NotRequired["aws_sdk_connect.types.ip_cidr_list.IpCidrList"]
    r"""<p>A list of IP address range strings that are allowed to access the instance. For more information on how to configure IP addresses, see<a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts\">Configure session timeouts</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    blocked_ips: NotRequired["aws_sdk_connect.types.ip_cidr_list.IpCidrList"]
    r"""<p>A list of IP address range strings that are blocked from accessing the instance. For more information on how to configure IP addresses, For more information on how to configure IP addresses, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac\">Configure IP-based access control</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    periodic_session_duration: NotRequired[
        "aws_sdk_connect.types.access_token_duration.AccessTokenDuration"
    ]
    r"""<p>The short lived session duration configuration for users logged in to Connect Customer, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, For more information on how to configure IP addresses, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts\">Configure session timeouts</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    session_inactivity_duration: NotRequired[
        "aws_sdk_connect.types.inactivity_duration.InactivityDuration"
    ]
    """<p>The period, in minutes, before an agent is automatically signed out of the contact center when they go inactive.</p>"""
    session_inactivity_handling_enabled: NotRequired[
        "aws_sdk_connect.types.boolean.Boolean"
    ]
    """<p>Determines if automatic logout on user inactivity is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuthenticationProfileRequest) -> dict:
    out: dict = {}
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
    if "periodic_session_duration" in value:
        out["PeriodicSessionDuration"] = value["periodic_session_duration"]
    if "session_inactivity_duration" in value:
        out["SessionInactivityDuration"] = value["session_inactivity_duration"]
    if "session_inactivity_handling_enabled" in value:
        out["SessionInactivityHandlingEnabled"] = value[
            "session_inactivity_handling_enabled"
        ]
    return out


def deserialize_json(data: dict) -> UpdateAuthenticationProfileRequest:
    out: UpdateAuthenticationProfileRequest = {}  # type: ignore[typeddict-item]
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
    if "PeriodicSessionDuration" in data:
        out["periodic_session_duration"] = data["PeriodicSessionDuration"]
    if "SessionInactivityDuration" in data:
        out["session_inactivity_duration"] = data["SessionInactivityDuration"]
    if "SessionInactivityHandlingEnabled" in data:
        out["session_inactivity_handling_enabled"] = data[
            "SessionInactivityHandlingEnabled"
        ]
    return out
