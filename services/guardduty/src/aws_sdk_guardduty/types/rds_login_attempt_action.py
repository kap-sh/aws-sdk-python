"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsLoginAttemptAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.login_attributes
    import aws_sdk_guardduty.types.remote_ip_details


class RdsLoginAttemptAction(TypedDict, closed=True):
    remote_ip_details: NotRequired[
        "aws_sdk_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    login_attributes: NotRequired[
        "aws_sdk_guardduty.types.login_attributes.LoginAttributes"
    ]
    """<p>Indicates the login attributes used in the login attempt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsLoginAttemptAction) -> dict:
    out: dict = {}
    if "remote_ip_details" in value:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = (
            aws_sdk_guardduty.types.remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    if "login_attributes" in value:
        import aws_sdk_guardduty.types.login_attributes

        out["LoginAttributes"] = (
            aws_sdk_guardduty.types.login_attributes.serialize_json(
                value["login_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RdsLoginAttemptAction:
    out: RdsLoginAttemptAction = {}  # type: ignore[typeddict-item]
    if "remoteIpDetails" in data:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            aws_sdk_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if "LoginAttributes" in data:
        import aws_sdk_guardduty.types.login_attributes

        out["login_attributes"] = (
            aws_sdk_guardduty.types.login_attributes.deserialize_json(
                data["LoginAttributes"]
            )
        )
    return out
