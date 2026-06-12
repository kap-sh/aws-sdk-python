"""Generated from Smithy shape ``com.amazonaws.configservice#AggregationAuthorization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.string


class AggregationAuthorization(TypedDict):
    aggregation_authorization_arn: NotRequired[
        "aws_sdk_config_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the aggregation object.</p>"""
    authorized_account_id: NotRequired[
        "aws_sdk_config_service.types.account_id.AccountId"
    ]
    """<p>The 12-digit account ID of the account authorized to aggregate data.</p>"""
    authorized_aws_region: NotRequired[
        "aws_sdk_config_service.types.aws_region.AwsRegion"
    ]
    """<p>The region authorized to collect aggregated data.</p>"""
    creation_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time stamp when the aggregation authorization was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationAuthorization) -> dict:
    out: dict = {}
    if "aggregation_authorization_arn" in value:
        out["AggregationAuthorizationArn"] = value["aggregation_authorization_arn"]
    if "authorized_account_id" in value:
        out["AuthorizedAccountId"] = value["authorized_account_id"]
    if "authorized_aws_region" in value:
        out["AuthorizedAwsRegion"] = value["authorized_aws_region"]
    if "creation_time" in value:
        import aws_sdk_config_service.types.date

        out["CreationTime"] = aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregationAuthorization:
    out: AggregationAuthorization = {}  # type: ignore[typeddict-item]
    if "AggregationAuthorizationArn" in data:
        out["aggregation_authorization_arn"] = data["AggregationAuthorizationArn"]
    if "AuthorizedAccountId" in data:
        out["authorized_account_id"] = data["AuthorizedAccountId"]
    if "AuthorizedAwsRegion" in data:
        out["authorized_aws_region"] = data["AuthorizedAwsRegion"]
    if "CreationTime" in data:
        import aws_sdk_config_service.types.date

        out["creation_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
