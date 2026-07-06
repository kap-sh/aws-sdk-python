"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageTopAccountsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_feature
    import aws_sdk_guardduty.types.usage_top_accounts_by_feature_list


class UsageTopAccountsResult(TypedDict, closed=True):
    feature: NotRequired["aws_sdk_guardduty.types.usage_feature.UsageFeature"]
    """<p>Features by which you can generate the usage statistics.</p> <p> <code>RDS_LOGIN_EVENTS</code> is currently not supported with <code>topAccountsByFeature</code>.</p>"""
    accounts: NotRequired[
        "aws_sdk_guardduty.types.usage_top_accounts_by_feature_list.UsageTopAccountsByFeatureList"
    ]
    """<p>The accounts that contributed to the total usage cost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageTopAccountsResult) -> dict:
    out: dict = {}
    if "feature" in value:
        import aws_sdk_guardduty.types.usage_feature

        out["feature"] = aws_sdk_guardduty.types.usage_feature.serialize_json(
            value["feature"]
        )
    if "accounts" in value:
        import aws_sdk_guardduty.types.usage_top_accounts_by_feature_list

        out["accounts"] = (
            aws_sdk_guardduty.types.usage_top_accounts_by_feature_list.serialize_json(
                value["accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> UsageTopAccountsResult:
    out: UsageTopAccountsResult = {}  # type: ignore[typeddict-item]
    if "feature" in data:
        import aws_sdk_guardduty.types.usage_feature

        out["feature"] = aws_sdk_guardduty.types.usage_feature.deserialize_json(
            data["feature"]
        )
    if "accounts" in data:
        import aws_sdk_guardduty.types.usage_top_accounts_by_feature_list

        out["accounts"] = (
            aws_sdk_guardduty.types.usage_top_accounts_by_feature_list.deserialize_json(
                data["accounts"]
            )
        )
    return out
