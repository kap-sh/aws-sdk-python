"""Generated from Smithy shape ``com.amazonaws.configservice#PutAggregationAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.tags_list


class PutAggregationAuthorizationRequest(TypedDict):
    authorized_account_id: "aws_sdk_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the account authorized to aggregate data.</p>"""
    authorized_aws_region: "aws_sdk_config_service.types.aws_region.AwsRegion"
    """<p>The region authorized to collect aggregated data.</p>"""
    tags: NotRequired["aws_sdk_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAggregationAuthorizationRequest) -> dict:
    out: dict = {}
    out["AuthorizedAccountId"] = value["authorized_account_id"]
    out["AuthorizedAwsRegion"] = value["authorized_aws_region"]
    if "tags" in value:
        import aws_sdk_config_service.types.tags_list

        out["Tags"] = aws_sdk_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAggregationAuthorizationRequest:
    out: PutAggregationAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "AuthorizedAccountId" in data:
        out["authorized_account_id"] = data["AuthorizedAccountId"]
    else:
        raise DeserializationError(
            "PutAggregationAuthorizationRequest.authorized_account_id required"
        )
    if "AuthorizedAwsRegion" in data:
        out["authorized_aws_region"] = data["AuthorizedAwsRegion"]
    else:
        raise DeserializationError(
            "PutAggregationAuthorizationRequest.authorized_aws_region required"
        )
    if "Tags" in data:
        import aws_sdk_config_service.types.tags_list

        out["tags"] = aws_sdk_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
