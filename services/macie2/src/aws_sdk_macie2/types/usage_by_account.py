"""Generated from Smithy shape ``com.amazonaws.macie2#UsageByAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.currency
    import aws_sdk_macie2.types.service_limit
    import aws_sdk_macie2.types.usage_type


class UsageByAccount(TypedDict, closed=True):
    currency: NotRequired["aws_sdk_macie2.types.currency.Currency"]
    """<p>The type of currency that the value for the metric (estimatedCost) is reported in.</p>"""
    estimated_cost: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The estimated value for the metric.</p>"""
    service_limit: NotRequired["aws_sdk_macie2.types.service_limit.ServiceLimit"]
    """<p>The current value for the quota that corresponds to the metric specified by the type field.</p>"""
    type: NotRequired["aws_sdk_macie2.types.usage_type.UsageType"]
    """<p>The name of the metric. Possible values are: AUTOMATED_OBJECT_MONITORING, to monitor S3 objects for automated sensitive data discovery; AUTOMATED_SENSITIVE_DATA_DISCOVERY, to analyze S3 objects for automated sensitive data discovery; DATA_INVENTORY_EVALUATION, to monitor S3 buckets; and, SENSITIVE_DATA_DISCOVERY, to run classification jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageByAccount) -> dict:
    out: dict = {}
    if "currency" in value:
        import aws_sdk_macie2.types.currency

        out["currency"] = aws_sdk_macie2.types.currency.serialize_json(
            value["currency"]
        )
    if "estimated_cost" in value:
        out["estimatedCost"] = value["estimated_cost"]
    if "service_limit" in value:
        import aws_sdk_macie2.types.service_limit

        out["serviceLimit"] = aws_sdk_macie2.types.service_limit.serialize_json(
            value["service_limit"]
        )
    if "type" in value:
        import aws_sdk_macie2.types.usage_type

        out["type"] = aws_sdk_macie2.types.usage_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UsageByAccount:
    out: UsageByAccount = {}  # type: ignore[typeddict-item]
    if "currency" in data:
        import aws_sdk_macie2.types.currency

        out["currency"] = aws_sdk_macie2.types.currency.deserialize_json(
            data["currency"]
        )
    if "estimatedCost" in data:
        out["estimated_cost"] = data["estimatedCost"]
    if "serviceLimit" in data:
        import aws_sdk_macie2.types.service_limit

        out["service_limit"] = aws_sdk_macie2.types.service_limit.deserialize_json(
            data["serviceLimit"]
        )
    if "type" in data:
        import aws_sdk_macie2.types.usage_type

        out["type"] = aws_sdk_macie2.types.usage_type.deserialize_json(data["type"])
    return out
