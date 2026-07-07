"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetUsageLimitRequest``."""

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError


class GetUsageLimitRequest(TypedDict, closed=True):
    usage_limit_id: "str"
    """<p>The unique identifier of the usage limit to return information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUsageLimitRequest) -> dict:
    out: dict = {}
    out["usageLimitId"] = value["usage_limit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUsageLimitRequest:
    out: GetUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if "usageLimitId" in data:
        out["usage_limit_id"] = data["usageLimitId"]
    else:
        raise DeserializationError("GetUsageLimitRequest.usage_limit_id required")
    return out
