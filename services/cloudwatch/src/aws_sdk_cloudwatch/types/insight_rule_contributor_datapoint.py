"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributorDatapoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_unbound_double
    import aws_sdk_cloudwatch.types.timestamp


class InsightRuleContributorDatapoint(TypedDict):
    timestamp: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The timestamp of the data point.</p>"""
    approximate_value: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The approximate value that this contributor added during this timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributorDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["Timestamp"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "approximate_value" in value:
        out["ApproximateValue"] = value["approximate_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRuleContributorDatapoint:
    out: InsightRuleContributorDatapoint = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if "ApproximateValue" in data:
        out["approximate_value"] = data["ApproximateValue"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributorDatapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "approximate_value" in value:
        pairs.append((f"{prefix}.ApproximateValue", str(value["approximate_value"])))


def deserialize_query(el: Element) -> InsightRuleContributorDatapoint:
    out: InsightRuleContributorDatapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_approximate_value = el.find("ApproximateValue")
    if child_approximate_value is not None:
        out["approximate_value"] = float(child_approximate_value.text or "")
    return out
