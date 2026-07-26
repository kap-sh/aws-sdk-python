"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateUsageLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.usage_limit


class UpdateUsageLimitResponse(TypedDict, closed=True):
    usage_limit: NotRequired["capo_redshift_serverless.types.usage_limit.UsageLimit"]
    """<p>The updated usage limit object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUsageLimitResponse) -> dict:
    out: dict = {}
    if "usage_limit" in value:
        import capo_redshift_serverless.types.usage_limit

        out["usageLimit"] = (
            capo_redshift_serverless.types.usage_limit.serialize_aws_json_1_1(
                value["usage_limit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUsageLimitResponse:
    out: UpdateUsageLimitResponse = {}  # type: ignore[typeddict-item]
    if "usageLimit" in data:
        import capo_redshift_serverless.types.usage_limit

        out["usage_limit"] = (
            capo_redshift_serverless.types.usage_limit.deserialize_aws_json_1_1(
                data["usageLimit"]
            )
        )
    return out
