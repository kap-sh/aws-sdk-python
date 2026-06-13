"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetUsageLimitResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.usage_limit


class GetUsageLimitResponse(TypedDict):
    usage_limit: NotRequired["aws_sdk_redshift_serverless.types.usage_limit.UsageLimit"]
    """<p>The returned usage limit object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUsageLimitResponse) -> dict:
    out: dict = {}
    if "usage_limit" in value:
        import aws_sdk_redshift_serverless.types.usage_limit

        out["usageLimit"] = (
            aws_sdk_redshift_serverless.types.usage_limit.serialize_aws_json_1_1(
                value["usage_limit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUsageLimitResponse:
    out: GetUsageLimitResponse = {}  # type: ignore[typeddict-item]
    if "usageLimit" in data:
        import aws_sdk_redshift_serverless.types.usage_limit

        out["usage_limit"] = (
            aws_sdk_redshift_serverless.types.usage_limit.deserialize_aws_json_1_1(
                data["usageLimit"]
            )
        )
    return out
