"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.data_source_list
    import aws_sdk_guardduty.types.resource_list
    import aws_sdk_guardduty.types.usage_feature_list


class UsageCriteria(TypedDict):
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>The account IDs to aggregate usage statistics from.</p>"""
    data_sources: NotRequired["aws_sdk_guardduty.types.data_source_list.DataSourceList"]
    """<p>The data sources to aggregate usage statistics from.</p>"""
    resources: NotRequired["aws_sdk_guardduty.types.resource_list.ResourceList"]
    """<p>The resources to aggregate usage statistics from. Only accepts exact resource names.</p>"""
    features: NotRequired["aws_sdk_guardduty.types.usage_feature_list.UsageFeatureList"]
    """<p>The features to aggregate usage statistics from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageCriteria) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    if "data_sources" in value:
        import aws_sdk_guardduty.types.data_source_list

        out["dataSources"] = aws_sdk_guardduty.types.data_source_list.serialize_json(
            value["data_sources"]
        )
    if "resources" in value:
        import aws_sdk_guardduty.types.resource_list

        out["resources"] = aws_sdk_guardduty.types.resource_list.serialize_json(
            value["resources"]
        )
    if "features" in value:
        import aws_sdk_guardduty.types.usage_feature_list

        out["features"] = aws_sdk_guardduty.types.usage_feature_list.serialize_json(
            value["features"]
        )
    return out


def deserialize_json(data: dict) -> UsageCriteria:
    out: UsageCriteria = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    if "dataSources" in data:
        import aws_sdk_guardduty.types.data_source_list

        out["data_sources"] = aws_sdk_guardduty.types.data_source_list.deserialize_json(
            data["dataSources"]
        )
    if "resources" in data:
        import aws_sdk_guardduty.types.resource_list

        out["resources"] = aws_sdk_guardduty.types.resource_list.deserialize_json(
            data["resources"]
        )
    if "features" in data:
        import aws_sdk_guardduty.types.usage_feature_list

        out["features"] = aws_sdk_guardduty.types.usage_feature_list.deserialize_json(
            data["features"]
        )
    return out
