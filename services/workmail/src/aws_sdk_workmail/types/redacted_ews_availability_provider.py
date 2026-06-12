"""Generated from Smithy shape ``com.amazonaws.workmail#RedactedEwsAvailabilityProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.external_user_name
    import aws_sdk_workmail.types.url


class RedactedEwsAvailabilityProvider(TypedDict):
    ews_endpoint: NotRequired["aws_sdk_workmail.types.url.Url"]
    """<p>The endpoint of the remote EWS server.</p>"""
    ews_username: NotRequired[
        "aws_sdk_workmail.types.external_user_name.ExternalUserName"
    ]
    """<p>The username used to authenticate the remote EWS server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedactedEwsAvailabilityProvider) -> dict:
    out: dict = {}
    if "ews_endpoint" in value:
        out["EwsEndpoint"] = value["ews_endpoint"]
    if "ews_username" in value:
        out["EwsUsername"] = value["ews_username"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedactedEwsAvailabilityProvider:
    out: RedactedEwsAvailabilityProvider = {}  # type: ignore[typeddict-item]
    if "EwsEndpoint" in data:
        out["ews_endpoint"] = data["EwsEndpoint"]
    if "EwsUsername" in data:
        out["ews_username"] = data["EwsUsername"]
    return out
