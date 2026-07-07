"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetIdentityCenterAuthTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class GetIdentityCenterAuthTokenResponse(TypedDict, closed=True):
    token: NotRequired["str"]
    """<p>The Identity Center authentication token that can be used to access data in the specified workgroups.</p> <p>This token contains the Identity Center identity information and is encrypted for secure transmission.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the Identity Center authentication token expires.</p> <p>After this time, a new token must be requested for continued access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityCenterAuthTokenResponse) -> dict:
    out: dict = {}
    if "token" in value:
        out["Token"] = value["token"]
    if "expiration_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["ExpirationTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityCenterAuthTokenResponse:
    out: GetIdentityCenterAuthTokenResponse = {}  # type: ignore[typeddict-item]
    if "Token" in data:
        out["token"] = data["Token"]
    if "ExpirationTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["expiration_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    return out
