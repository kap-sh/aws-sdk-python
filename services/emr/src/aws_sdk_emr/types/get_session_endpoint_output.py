"""Generated from Smithy shape ``com.amazonaws.emr#GetSessionEndpointOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.credentials
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.sensitive_string
    import aws_sdk_emr.types.xml_string


class GetSessionEndpointOutput(TypedDict):
    endpoint: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Spark Connect endpoint URL to use in the PySpark client.</p>"""
    auth_token: NotRequired["aws_sdk_emr.types.sensitive_string.SensitiveString"]
    """<p>A time-limited authentication token used to connect to the Spark Connect endpoint.</p>"""
    auth_token_expiration_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time at which the authentication token expires. After this time, call <code>GetSessionEndpoint</code> again to obtain a new token.</p>"""
    credentials: NotRequired["aws_sdk_emr.types.credentials.Credentials"]
    """<p>Username and password used to authenticate with the Spark Connect server when connecting directly over VPC peering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointOutput) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "auth_token" in value:
        out["AuthToken"] = value["auth_token"]
    if "auth_token_expiration_time" in value:
        import aws_sdk_emr.types.date

        out["AuthTokenExpirationTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["auth_token_expiration_time"]
        )
    if "credentials" in value:
        import aws_sdk_emr.types.credentials

        out["Credentials"] = aws_sdk_emr.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointOutput:
    out: GetSessionEndpointOutput = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "AuthToken" in data:
        out["auth_token"] = data["AuthToken"]
    if "AuthTokenExpirationTime" in data:
        import aws_sdk_emr.types.date

        out["auth_token_expiration_time"] = (
            aws_sdk_emr.types.date.deserialize_aws_json_1_1(
                data["AuthTokenExpirationTime"]
            )
        )
    if "Credentials" in data:
        import aws_sdk_emr.types.credentials

        out["credentials"] = aws_sdk_emr.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    return out
