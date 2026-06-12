"""Generated from Smithy shape ``com.amazonaws.emr#GetClusterSessionCredentialsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.credentials
    import aws_sdk_emr.types.date


class GetClusterSessionCredentialsOutput(TypedDict):
    credentials: NotRequired["aws_sdk_emr.types.credentials.Credentials"]
    """<p>The credentials that you can use to connect to cluster endpoints that support username and password authentication.</p>"""
    expires_at: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time when the credentials that are returned by the <code>GetClusterSessionCredentials</code> API expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClusterSessionCredentialsOutput) -> dict:
    out: dict = {}
    if "credentials" in value:
        import aws_sdk_emr.types.credentials

        out["Credentials"] = aws_sdk_emr.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    if "expires_at" in value:
        import aws_sdk_emr.types.date

        out["ExpiresAt"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["expires_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClusterSessionCredentialsOutput:
    out: GetClusterSessionCredentialsOutput = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import aws_sdk_emr.types.credentials

        out["credentials"] = aws_sdk_emr.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    if "ExpiresAt" in data:
        import aws_sdk_emr.types.date

        out["expires_at"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["ExpiresAt"]
        )
    return out
