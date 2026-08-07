"""Generated from Smithy shape ``com.amazonaws.redshift#CreateUsageLimitMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.long
    import capo_redshift.types.string
    import capo_redshift.types.tag_list
    import capo_redshift.types.usage_limit_breach_action
    import capo_redshift.types.usage_limit_feature_type
    import capo_redshift.types.usage_limit_limit_type
    import capo_redshift.types.usage_limit_period


class CreateUsageLimitMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster that you want to limit usage.</p>"""
    feature_type: NotRequired[
        "capo_redshift.types.usage_limit_feature_type.UsageLimitFeatureType"
    ]
    """<p>The Amazon Redshift feature that you want to limit.</p>"""
    limit_type: NotRequired[
        "capo_redshift.types.usage_limit_limit_type.UsageLimitLimitType"
    ]
    """<p>The type of limit. Depending on the feature type, this can be based on a time duration or data size. If <code>FeatureType</code> is <code>spectrum</code>, then <code>LimitType</code> must be <code>data-scanned</code>. If <code>FeatureType</code> is <code>concurrency-scaling</code>, then <code>LimitType</code> must be <code>time</code>. If <code>FeatureType</code> is <code>cross-region-datasharing</code>, then <code>LimitType</code> must be <code>data-scanned</code>. If <code>FeatureType</code> is <code>extra-compute-for-automatic-optimization</code>, then <code>LimitType</code> must be <code>time</code>. </p>"""
    amount: NotRequired["capo_redshift.types.long.Long"]
    """<p>The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB). The value must be a positive number. </p>"""
    period: NotRequired["capo_redshift.types.usage_limit_period.UsageLimitPeriod"]
    """<p>The time period that the amount applies to. A <code>weekly</code> period begins on Sunday. The default is <code>monthly</code>. </p>"""
    breach_action: NotRequired[
        "capo_redshift.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The action that Amazon Redshift takes when the limit is reached. The default is log. For more information about this parameter, see <a>UsageLimit</a>.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUsageLimitMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "feature_type" in value:
        import capo_redshift.types.usage_limit_feature_type

        capo_redshift.types.usage_limit_feature_type.serialize_query(
            value["feature_type"], pairs, f"{key_prefix}FeatureType"
        )
    if "limit_type" in value:
        import capo_redshift.types.usage_limit_limit_type

        capo_redshift.types.usage_limit_limit_type.serialize_query(
            value["limit_type"], pairs, f"{key_prefix}LimitType"
        )
    if "amount" in value:
        pairs.append((f"{key_prefix}Amount", str(value["amount"])))
    if "period" in value:
        import capo_redshift.types.usage_limit_period

        capo_redshift.types.usage_limit_period.serialize_query(
            value["period"], pairs, f"{key_prefix}Period"
        )
    if "breach_action" in value:
        import capo_redshift.types.usage_limit_breach_action

        capo_redshift.types.usage_limit_breach_action.serialize_query(
            value["breach_action"], pairs, f"{key_prefix}BreachAction"
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateUsageLimitMessage:
    out: CreateUsageLimitMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_feature_type = el.find("FeatureType")
    if child_feature_type is not None:
        import capo_redshift.types.usage_limit_feature_type

        out["feature_type"] = (
            capo_redshift.types.usage_limit_feature_type.deserialize_query(
                child_feature_type
            )
        )
    child_limit_type = el.find("LimitType")
    if child_limit_type is not None:
        import capo_redshift.types.usage_limit_limit_type

        out["limit_type"] = (
            capo_redshift.types.usage_limit_limit_type.deserialize_query(
                child_limit_type
            )
        )
    child_amount = el.find("Amount")
    if child_amount is not None:
        out["amount"] = int(child_amount.text or "")
    child_period = el.find("Period")
    if child_period is not None:
        import capo_redshift.types.usage_limit_period

        out["period"] = capo_redshift.types.usage_limit_period.deserialize_query(
            child_period
        )
    child_breach_action = el.find("BreachAction")
    if child_breach_action is not None:
        import capo_redshift.types.usage_limit_breach_action

        out["breach_action"] = (
            capo_redshift.types.usage_limit_breach_action.deserialize_query(
                child_breach_action
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    return out
