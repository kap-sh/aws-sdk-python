"""Generated from Smithy shape ``com.amazonaws.macie2#UsageTotal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.currency
    import aws_sdk_macie2.types.usage_type


class UsageTotal(TypedDict):
    currency: NotRequired["aws_sdk_macie2.types.currency.Currency"]
    """<p>The type of currency that the value for the metric (estimatedCost) is reported in.</p>"""
    estimated_cost: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The estimated value for the metric.</p>"""
    type: NotRequired["aws_sdk_macie2.types.usage_type.UsageType"]
    """<p>The name of the metric. Possible values are: AUTOMATED_OBJECT_MONITORING, to monitor S3 objects for automated sensitive data discovery; AUTOMATED_SENSITIVE_DATA_DISCOVERY, to analyze S3 objects for automated sensitive data discovery; DATA_INVENTORY_EVALUATION, to monitor S3 buckets; and, SENSITIVE_DATA_DISCOVERY, to run classification jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageTotal) -> dict:
    out: dict = {}
    if "currency" in value:
        import aws_sdk_macie2.types.currency

        out["currency"] = aws_sdk_macie2.types.currency.serialize_json(
            value["currency"]
        )
    if "estimated_cost" in value:
        out["estimatedCost"] = value["estimated_cost"]
    if "type" in value:
        import aws_sdk_macie2.types.usage_type

        out["type"] = aws_sdk_macie2.types.usage_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UsageTotal:
    out: UsageTotal = {}  # type: ignore[typeddict-item]
    if "currency" in data:
        import aws_sdk_macie2.types.currency

        out["currency"] = aws_sdk_macie2.types.currency.deserialize_json(
            data["currency"]
        )
    if "estimatedCost" in data:
        out["estimated_cost"] = data["estimatedCost"]
    if "type" in data:
        import aws_sdk_macie2.types.usage_type

        out["type"] = aws_sdk_macie2.types.usage_type.deserialize_json(data["type"])
    return out
