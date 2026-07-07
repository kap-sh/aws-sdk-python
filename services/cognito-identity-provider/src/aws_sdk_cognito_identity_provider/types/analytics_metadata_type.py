"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AnalyticsMetadataType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class AnalyticsMetadataType(TypedDict, closed=True):
    analytics_endpoint_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The endpoint ID. Information that you want to pass to Amazon Pinpoint about where to send notifications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyticsMetadataType) -> dict:
    out: dict = {}
    if "analytics_endpoint_id" in value:
        out["AnalyticsEndpointId"] = value["analytics_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyticsMetadataType:
    out: AnalyticsMetadataType = {}  # type: ignore[typeddict-item]
    if "AnalyticsEndpointId" in data:
        out["analytics_endpoint_id"] = data["AnalyticsEndpointId"]
    return out
