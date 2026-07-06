"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContributorInsightsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.contributor_insights_action
    import aws_sdk_dynamodb.types.contributor_insights_mode
    import aws_sdk_dynamodb.types.index_name
    import aws_sdk_dynamodb.types.table_arn


class UpdateContributorInsightsInput(TypedDict, closed=True):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["aws_sdk_dynamodb.types.index_name.IndexName"]
    """<p>The global secondary index name, if applicable.</p>"""
    contributor_insights_action: (
        "aws_sdk_dynamodb.types.contributor_insights_action.ContributorInsightsAction"
    )
    """<p>Represents the contributor insights action.</p>"""
    contributor_insights_mode: NotRequired[
        "aws_sdk_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>Specifies whether to track all access and throttled events or throttled events only for the DynamoDB table or index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContributorInsightsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    import aws_sdk_dynamodb.types.contributor_insights_action

    out["ContributorInsightsAction"] = (
        aws_sdk_dynamodb.types.contributor_insights_action.serialize_aws_json_1_0(
            value["contributor_insights_action"]
        )
    )
    if "contributor_insights_mode" in value:
        import aws_sdk_dynamodb.types.contributor_insights_mode

        out["ContributorInsightsMode"] = (
            aws_sdk_dynamodb.types.contributor_insights_mode.serialize_aws_json_1_0(
                value["contributor_insights_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContributorInsightsInput:
    out: UpdateContributorInsightsInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdateContributorInsightsInput.table_name required")
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ContributorInsightsAction" in data:
        import aws_sdk_dynamodb.types.contributor_insights_action

        out["contributor_insights_action"] = (
            aws_sdk_dynamodb.types.contributor_insights_action.deserialize_aws_json_1_0(
                data["ContributorInsightsAction"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateContributorInsightsInput.contributor_insights_action required"
        )
    if "ContributorInsightsMode" in data:
        import aws_sdk_dynamodb.types.contributor_insights_mode

        out["contributor_insights_mode"] = (
            aws_sdk_dynamodb.types.contributor_insights_mode.deserialize_aws_json_1_0(
                data["ContributorInsightsMode"]
            )
        )
    return out
