"""Generated from Smithy shape ``com.amazonaws.configservice#PutAggregationAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.tags_list


class PutAggregationAuthorizationRequest(TypedDict, closed=True):
    authorized_account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the account authorized to aggregate data.</p>"""
    authorized_aws_region: "capo_config_service.types.aws_region.AwsRegion"
    """<p>The region authorized to collect aggregated data.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAggregationAuthorizationRequest) -> dict:
    out: dict = {}
    out["AuthorizedAccountId"] = value["authorized_account_id"]
    out["AuthorizedAwsRegion"] = value["authorized_aws_region"]
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
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
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
