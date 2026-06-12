"""Generated from Smithy shape ``com.amazonaws.workmail#EwsAvailabilityProvider``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.external_user_name
    import aws_sdk_workmail.types.password
    import aws_sdk_workmail.types.url


class EwsAvailabilityProvider(TypedDict):
    ews_endpoint: "aws_sdk_workmail.types.url.Url"
    """<p>The endpoint of the remote EWS server.</p>"""
    ews_username: "aws_sdk_workmail.types.external_user_name.ExternalUserName"
    """<p>The username used to authenticate the remote EWS server.</p>"""
    ews_password: "aws_sdk_workmail.types.password.Password"
    """<p>The password used to authenticate the remote EWS server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EwsAvailabilityProvider) -> dict:
    out: dict = {}
    out["EwsEndpoint"] = value["ews_endpoint"]
    out["EwsUsername"] = value["ews_username"]
    out["EwsPassword"] = value["ews_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EwsAvailabilityProvider:
    out: EwsAvailabilityProvider = {}  # type: ignore[typeddict-item]
    if "EwsEndpoint" in data:
        out["ews_endpoint"] = data["EwsEndpoint"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_endpoint required")
    if "EwsUsername" in data:
        out["ews_username"] = data["EwsUsername"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_username required")
    if "EwsPassword" in data:
        out["ews_password"] = data["EwsPassword"]
    else:
        raise DeserializationError("EwsAvailabilityProvider.ews_password required")
    return out
