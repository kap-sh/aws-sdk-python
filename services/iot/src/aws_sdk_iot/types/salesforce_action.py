"""Generated from Smithy shape ``com.amazonaws.iot#SalesforceAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.salesforce_endpoint
    import aws_sdk_iot.types.salesforce_token


class SalesforceAction(TypedDict):
    token: "aws_sdk_iot.types.salesforce_token.SalesforceToken"
    """<p>The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.</p>"""
    url: "aws_sdk_iot.types.salesforce_endpoint.SalesforceEndpoint"
    """<p>The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceAction) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SalesforceAction:
    out: SalesforceAction = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("SalesforceAction.token required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("SalesforceAction.url required")
    return out
