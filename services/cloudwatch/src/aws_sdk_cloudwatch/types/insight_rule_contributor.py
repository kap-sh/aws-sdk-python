"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints
    import aws_sdk_cloudwatch.types.insight_rule_contributor_keys
    import aws_sdk_cloudwatch.types.insight_rule_unbound_double


class InsightRuleContributor(TypedDict):
    keys: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_contributor_keys.InsightRuleContributorKeys"
    ]
    """<p>One of the log entry field keywords that is used to define contributors for this rule.</p>"""
    approximate_aggregate_value: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>An approximation of the aggregate value that comes from this contributor.</p>"""
    datapoints: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints.InsightRuleContributorDatapoints"
    ]
    """<p>An array of the data points where this contributor is present. Only the data points when this contributor appeared are included in the array.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributor) -> dict:
    out: dict = {}
    if "keys" in value:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_keys

        out["Keys"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_keys.serialize_aws_json_1_0(
                value["keys"]
            )
        )
    if "approximate_aggregate_value" in value:
        out["ApproximateAggregateValue"] = value["approximate_aggregate_value"]
    if "datapoints" in value:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints

        out["Datapoints"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints.serialize_aws_json_1_0(
                value["datapoints"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRuleContributor:
    out: InsightRuleContributor = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_keys

        out["keys"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_keys.deserialize_aws_json_1_0(
                data["Keys"]
            )
        )
    if "ApproximateAggregateValue" in data:
        out["approximate_aggregate_value"] = data["ApproximateAggregateValue"]
    if "Datapoints" in data:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints

        out["datapoints"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints.deserialize_aws_json_1_0(
                data["Datapoints"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributor, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "keys" in value:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_keys

        aws_sdk_cloudwatch.types.insight_rule_contributor_keys.serialize_query(
            value["keys"], pairs, f"{prefix}.Keys"
        )
    if "approximate_aggregate_value" in value:
        pairs.append(
            (
                f"{prefix}.ApproximateAggregateValue",
                str(value["approximate_aggregate_value"]),
            )
        )
    if "datapoints" in value:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints

        aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints.serialize_query(
            value["datapoints"], pairs, f"{prefix}.Datapoints"
        )


def deserialize_query(el: Element) -> InsightRuleContributor:
    out: InsightRuleContributor = {}  # type: ignore[typeddict-item]
    child_keys = el.find("Keys")
    if child_keys is not None:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_keys

        out["keys"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_keys.deserialize_query(
                child_keys
            )
        )
    child_approximate_aggregate_value = el.find("ApproximateAggregateValue")
    if child_approximate_aggregate_value is not None:
        out["approximate_aggregate_value"] = float(
            child_approximate_aggregate_value.text or ""
        )
    child_datapoints = el.find("Datapoints")
    if child_datapoints is not None:
        import aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints

        out["datapoints"] = (
            aws_sdk_cloudwatch.types.insight_rule_contributor_datapoints.deserialize_query(
                child_datapoints
            )
        )
    return out
