"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateMemberDetectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.data_source_configurations
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.member_features_configurations


class UpdateMemberDetectorsRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The detector ID of the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>A list of member account IDs to be updated.</p>"""
    data_sources: NotRequired[
        "aws_sdk_guardduty.types.data_source_configurations.DataSourceConfigurations"
    ]
    """<p>Describes which data sources will be updated.</p>"""
    features: NotRequired[
        "aws_sdk_guardduty.types.member_features_configurations.MemberFeaturesConfigurations"
    ]
    """<p>A list of features that will be updated for the specified member accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemberDetectorsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    if "data_sources" in value:
        import aws_sdk_guardduty.types.data_source_configurations

        out["dataSources"] = (
            aws_sdk_guardduty.types.data_source_configurations.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import aws_sdk_guardduty.types.member_features_configurations

        out["features"] = (
            aws_sdk_guardduty.types.member_features_configurations.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMemberDetectorsRequest:
    out: UpdateMemberDetectorsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    if "dataSources" in data:
        import aws_sdk_guardduty.types.data_source_configurations

        out["data_sources"] = (
            aws_sdk_guardduty.types.data_source_configurations.deserialize_json(
                data["dataSources"]
            )
        )
    if "features" in data:
        import aws_sdk_guardduty.types.member_features_configurations

        out["features"] = (
            aws_sdk_guardduty.types.member_features_configurations.deserialize_json(
                data["features"]
            )
        )
    return out
