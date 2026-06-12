"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListMetricsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.account_id
    import aws_sdk_cloudwatch.types.dimension_filters
    import aws_sdk_cloudwatch.types.include_linked_accounts
    import aws_sdk_cloudwatch.types.metric_name
    import aws_sdk_cloudwatch.types.namespace
    import aws_sdk_cloudwatch.types.next_token
    import aws_sdk_cloudwatch.types.recently_active


class ListMetricsInput(TypedDict):
    namespace: NotRequired["aws_sdk_cloudwatch.types.namespace.Namespace"]
    """<p>The metric namespace to filter against. Only the namespace that matches exactly will be returned.</p>"""
    metric_name: NotRequired["aws_sdk_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric to filter against. Only the metrics with names that match exactly will be returned.</p>"""
    dimensions: NotRequired[
        "aws_sdk_cloudwatch.types.dimension_filters.DimensionFilters"
    ]
    """<p>The dimensions to filter against. Only the dimension with names that match exactly will be returned. If you specify one dimension name and a metric has that dimension and also other dimensions, it will be returned.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""
    recently_active: NotRequired[
        "aws_sdk_cloudwatch.types.recently_active.RecentlyActive"
    ]
    """<p>To filter the results to show only metrics that have had data points published in the past three hours, specify this parameter with a value of <code>PT3H</code>. This is the only valid value for this parameter.</p> <p>The results that are returned are an approximation of the value you specify. There is a low probability that the returned results include metrics with last published data as much as 50 minutes more than the specified time interval.</p>"""
    include_linked_accounts: NotRequired[
        "aws_sdk_cloudwatch.types.include_linked_accounts.IncludeLinkedAccounts"
    ]
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include metrics from source accounts in the returned data.</p> <p>The default is <code>false</code>.</p>"""
    owning_account: NotRequired["aws_sdk_cloudwatch.types.account_id.AccountId"]
    """<p>When you use this operation in a monitoring account, use this field to return metrics only from one source account. To do so, specify that source account ID in this field, and also specify <code>true</code> for <code>IncludeLinkedAccounts</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMetricsInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimension_filters

        out["Dimensions"] = (
            aws_sdk_cloudwatch.types.dimension_filters.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recently_active" in value:
        import aws_sdk_cloudwatch.types.recently_active

        out["RecentlyActive"] = (
            aws_sdk_cloudwatch.types.recently_active.serialize_aws_json_1_0(
                value["recently_active"]
            )
        )
    if "include_linked_accounts" in value:
        out["IncludeLinkedAccounts"] = value["include_linked_accounts"]
    if "owning_account" in value:
        out["OwningAccount"] = value["owning_account"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMetricsInput:
    out: ListMetricsInput = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Dimensions" in data:
        import aws_sdk_cloudwatch.types.dimension_filters

        out["dimensions"] = (
            aws_sdk_cloudwatch.types.dimension_filters.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecentlyActive" in data:
        import aws_sdk_cloudwatch.types.recently_active

        out["recently_active"] = (
            aws_sdk_cloudwatch.types.recently_active.deserialize_aws_json_1_0(
                data["RecentlyActive"]
            )
        )
    if "IncludeLinkedAccounts" in data:
        out["include_linked_accounts"] = data["IncludeLinkedAccounts"]
    if "OwningAccount" in data:
        out["owning_account"] = data["OwningAccount"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListMetricsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "namespace" in value:
        pairs.append((f"{prefix}.Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{prefix}.MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import aws_sdk_cloudwatch.types.dimension_filters

        aws_sdk_cloudwatch.types.dimension_filters.serialize_query(
            value["dimensions"], pairs, f"{prefix}.Dimensions"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "recently_active" in value:
        import aws_sdk_cloudwatch.types.recently_active

        aws_sdk_cloudwatch.types.recently_active.serialize_query(
            value["recently_active"], pairs, f"{prefix}.RecentlyActive"
        )
    if "include_linked_accounts" in value:
        pairs.append(
            (
                f"{prefix}.IncludeLinkedAccounts",
                "true" if value["include_linked_accounts"] else "false",
            )
        )
    if "owning_account" in value:
        pairs.append((f"{prefix}.OwningAccount", str(value["owning_account"])))


def deserialize_query(el: Element) -> ListMetricsInput:
    out: ListMetricsInput = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import aws_sdk_cloudwatch.types.dimension_filters

        out["dimensions"] = (
            aws_sdk_cloudwatch.types.dimension_filters.deserialize_query(
                child_dimensions
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_recently_active = el.find("RecentlyActive")
    if child_recently_active is not None:
        import aws_sdk_cloudwatch.types.recently_active

        out["recently_active"] = (
            aws_sdk_cloudwatch.types.recently_active.deserialize_query(
                child_recently_active
            )
        )
    child_include_linked_accounts = el.find("IncludeLinkedAccounts")
    if child_include_linked_accounts is not None:
        out["include_linked_accounts"] = (
            child_include_linked_accounts.text or ""
        ).lower() == "true"
    child_owning_account = el.find("OwningAccount")
    if child_owning_account is not None:
        out["owning_account"] = str(child_owning_account.text or "")
    return out
