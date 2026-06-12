"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleMetricDatapoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_unbound_double
    import aws_sdk_cloudwatch.types.timestamp


class InsightRuleMetricDatapoint(TypedDict):
    timestamp: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The timestamp of the data point.</p>"""
    unique_contributors: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The number of unique contributors who published data during this timestamp.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    max_contributor_value: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The maximum value provided by one contributor during this timestamp. Each timestamp is evaluated separately, so the identity of the max contributor could be different for each timestamp.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    sample_count: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The number of occurrences that matched the rule during this data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    average: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The average value from all contributors during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    sum: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The sum of the values from all contributors during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    minimum: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The minimum value from a single contributor during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    maximum: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The maximum value from a single occurence from a single contributor during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleMetricDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["Timestamp"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "unique_contributors" in value:
        out["UniqueContributors"] = value["unique_contributors"]
    if "max_contributor_value" in value:
        out["MaxContributorValue"] = value["max_contributor_value"]
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
    if "average" in value:
        out["Average"] = value["average"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRuleMetricDatapoint:
    out: InsightRuleMetricDatapoint = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if "UniqueContributors" in data:
        out["unique_contributors"] = data["UniqueContributors"]
    if "MaxContributorValue" in data:
        out["max_contributor_value"] = data["MaxContributorValue"]
    if "SampleCount" in data:
        out["sample_count"] = data["SampleCount"]
    if "Average" in data:
        out["average"] = data["Average"]
    if "Sum" in data:
        out["sum"] = data["Sum"]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleMetricDatapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "timestamp" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "unique_contributors" in value:
        pairs.append(
            (f"{prefix}.UniqueContributors", str(value["unique_contributors"]))
        )
    if "max_contributor_value" in value:
        pairs.append(
            (f"{prefix}.MaxContributorValue", str(value["max_contributor_value"]))
        )
    if "sample_count" in value:
        pairs.append((f"{prefix}.SampleCount", str(value["sample_count"])))
    if "average" in value:
        pairs.append((f"{prefix}.Average", str(value["average"])))
    if "sum" in value:
        pairs.append((f"{prefix}.Sum", str(value["sum"])))
    if "minimum" in value:
        pairs.append((f"{prefix}.Minimum", str(value["minimum"])))
    if "maximum" in value:
        pairs.append((f"{prefix}.Maximum", str(value["maximum"])))


def deserialize_query(el: Element) -> InsightRuleMetricDatapoint:
    out: InsightRuleMetricDatapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["timestamp"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_unique_contributors = el.find("UniqueContributors")
    if child_unique_contributors is not None:
        out["unique_contributors"] = float(child_unique_contributors.text or "")
    child_max_contributor_value = el.find("MaxContributorValue")
    if child_max_contributor_value is not None:
        out["max_contributor_value"] = float(child_max_contributor_value.text or "")
    child_sample_count = el.find("SampleCount")
    if child_sample_count is not None:
        out["sample_count"] = float(child_sample_count.text or "")
    child_average = el.find("Average")
    if child_average is not None:
        out["average"] = float(child_average.text or "")
    child_sum = el.find("Sum")
    if child_sum is not None:
        out["sum"] = float(child_sum.text or "")
    child_minimum = el.find("Minimum")
    if child_minimum is not None:
        out["minimum"] = float(child_minimum.text or "")
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = float(child_maximum.text or "")
    return out
