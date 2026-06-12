"""Generated from Smithy shape ``com.amazonaws.glue#GetDashboardUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.sensitive_url


class GetDashboardUrlResponse(TypedDict):
    url: "aws_sdk_glue.types.sensitive_url.SensitiveUrl"
    """<p>The URL for the Spark monitoring dashboard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDashboardUrlResponse) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDashboardUrlResponse:
    out: GetDashboardUrlResponse = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("GetDashboardUrlResponse.url required")
    return out
