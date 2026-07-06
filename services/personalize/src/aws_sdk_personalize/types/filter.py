"""Generated from Smithy shape ``com.amazonaws.personalize#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.filter_expression
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class Filter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the filter.</p>"""
    filter_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the filter.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The time at which the filter was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The time at which the filter was last updated.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset group to which the filter belongs.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If the filter failed, the reason for its failure.</p>"""
    filter_expression: NotRequired[
        "aws_sdk_personalize.types.filter_expression.FilterExpression"
    ]
    r"""<p>Specifies the type of item interactions to filter out of recommendation results. The filter expression must follow specific format rules. For information about filter expression structure and syntax, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html\">Filter expressions</a>.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "filter_expression" in value:
        out["filterExpression"] = value["filter_expression"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "filterExpression" in data:
        out["filter_expression"] = data["filterExpression"]
    if "status" in data:
        out["status"] = data["status"]
    return out
