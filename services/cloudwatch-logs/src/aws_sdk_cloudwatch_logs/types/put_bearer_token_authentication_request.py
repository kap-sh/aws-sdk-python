"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutBearerTokenAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.bearer_token_authentication_enabled
    import aws_sdk_cloudwatch_logs.types.log_group_identifier


class PutBearerTokenAuthenticationRequest(TypedDict):
    log_group_identifier: (
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    r"""<p>The name or ARN of the log group.</p> <p>Type: String</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512.</p> <p>Pattern: <code>[\.\-_/#A-Za-z0-9]+</code> </p> <p>Required: Yes</p>"""
    bearer_token_authentication_enabled: "aws_sdk_cloudwatch_logs.types.bearer_token_authentication_enabled.BearerTokenAuthenticationEnabled"
    """<p>Whether to enable bearer token authentication.</p> <p>Type: Boolean</p> <p>Required: Yes</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutBearerTokenAuthenticationRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    out["bearerTokenAuthenticationEnabled"] = value[
        "bearer_token_authentication_enabled"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutBearerTokenAuthenticationRequest:
    out: PutBearerTokenAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        raise DeserializationError(
            "PutBearerTokenAuthenticationRequest.log_group_identifier required"
        )
    if "bearerTokenAuthenticationEnabled" in data:
        out["bearer_token_authentication_enabled"] = data[
            "bearerTokenAuthenticationEnabled"
        ]
    else:
        raise DeserializationError(
            "PutBearerTokenAuthenticationRequest.bearer_token_authentication_enabled required"
        )
    return out
