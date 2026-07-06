"""Generated from Smithy shape ``com.amazonaws.apigateway#QuotaSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.integer
    import aws_sdk_api_gateway.types.quota_period_type


class QuotaSettings(TypedDict, closed=True):
    limit: "aws_sdk_api_gateway.types.integer.Integer"
    """<p>The target maximum number of requests that can be made in a given time period.</p>"""
    offset: "aws_sdk_api_gateway.types.integer.Integer"
    """<p>The number of requests subtracted from the given limit in the initial time period.</p>"""
    period: NotRequired["aws_sdk_api_gateway.types.quota_period_type.QuotaPeriodType"]
    r"""<p>The time period in which the limit applies. Valid values are \"DAY\", \"WEEK\" or \"MONTH\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaSettings) -> dict:
    out: dict = {}
    out["limit"] = value.get("limit", 0)
    out["offset"] = value.get("offset", 0)
    if "period" in value:
        import aws_sdk_api_gateway.types.quota_period_type

        out["period"] = aws_sdk_api_gateway.types.quota_period_type.serialize_json(
            value["period"]
        )
    return out


def deserialize_json(data: dict) -> QuotaSettings:
    out: QuotaSettings = {}  # type: ignore[typeddict-item]
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if "offset" in data:
        out["offset"] = data["offset"]
    else:
        out["offset"] = 0
    if "period" in data:
        import aws_sdk_api_gateway.types.quota_period_type

        out["period"] = aws_sdk_api_gateway.types.quota_period_type.deserialize_json(
            data["period"]
        )
    return out
