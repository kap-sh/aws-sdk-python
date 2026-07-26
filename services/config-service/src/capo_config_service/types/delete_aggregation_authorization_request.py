"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteAggregationAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region


class DeleteAggregationAuthorizationRequest(TypedDict, closed=True):
    authorized_account_id: "capo_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the account authorized to aggregate data.</p>"""
    authorized_aws_region: "capo_config_service.types.aws_region.AwsRegion"
    """<p>The region authorized to collect aggregated data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAggregationAuthorizationRequest) -> dict:
    out: dict = {}
    out["AuthorizedAccountId"] = value["authorized_account_id"]
    out["AuthorizedAwsRegion"] = value["authorized_aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAggregationAuthorizationRequest:
    out: DeleteAggregationAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "AuthorizedAccountId" in data:
        out["authorized_account_id"] = data["AuthorizedAccountId"]
    else:
        raise DeserializationError(
            "DeleteAggregationAuthorizationRequest.authorized_account_id required"
        )
    if "AuthorizedAwsRegion" in data:
        out["authorized_aws_region"] = data["AuthorizedAwsRegion"]
    else:
        raise DeserializationError(
            "DeleteAggregationAuthorizationRequest.authorized_aws_region required"
        )
    return out
