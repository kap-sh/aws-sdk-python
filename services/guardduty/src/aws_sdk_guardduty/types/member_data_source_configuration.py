"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberDataSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.data_source_configurations_result
    import aws_sdk_guardduty.types.member_features_configurations_results


class MemberDataSourceConfiguration(TypedDict):
    account_id: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The account ID for the member account.</p>"""
    data_sources: NotRequired[
        "aws_sdk_guardduty.types.data_source_configurations_result.DataSourceConfigurationsResult"
    ]
    """<p>Contains information on the status of data sources for the account.</p>"""
    features: NotRequired[
        "aws_sdk_guardduty.types.member_features_configurations_results.MemberFeaturesConfigurationsResults"
    ]
    """<p>Contains information about the status of the features for the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberDataSourceConfiguration) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "data_sources" in value:
        import aws_sdk_guardduty.types.data_source_configurations_result

        out["dataSources"] = (
            aws_sdk_guardduty.types.data_source_configurations_result.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import aws_sdk_guardduty.types.member_features_configurations_results

        out["features"] = (
            aws_sdk_guardduty.types.member_features_configurations_results.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberDataSourceConfiguration:
    out: MemberDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "dataSources" in data:
        import aws_sdk_guardduty.types.data_source_configurations_result

        out["data_sources"] = (
            aws_sdk_guardduty.types.data_source_configurations_result.deserialize_json(
                data["dataSources"]
            )
        )
    if "features" in data:
        import aws_sdk_guardduty.types.member_features_configurations_results

        out["features"] = (
            aws_sdk_guardduty.types.member_features_configurations_results.deserialize_json(
                data["features"]
            )
        )
    return out
