"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteUsageLimitRequest``."""

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError


class DeleteUsageLimitRequest(TypedDict, closed=True):
    usage_limit_id: "str"
    """<p>The unique identifier of the usage limit to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUsageLimitRequest) -> dict:
    out: dict = {}
    out["usageLimitId"] = value["usage_limit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUsageLimitRequest:
    out: DeleteUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if "usageLimitId" in data:
        out["usage_limit_id"] = data["usageLimitId"]
    else:
        raise DeserializationError("DeleteUsageLimitRequest.usage_limit_id required")
    return out
