"""Generated from Smithy shape ``com.amazonaws.configservice#PutAggregationAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregation_authorization


class PutAggregationAuthorizationResponse(TypedDict, closed=True):
    aggregation_authorization: NotRequired[
        "aws_sdk_config_service.types.aggregation_authorization.AggregationAuthorization"
    ]
    """<p>Returns an AggregationAuthorization object. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAggregationAuthorizationResponse) -> dict:
    out: dict = {}
    if "aggregation_authorization" in value:
        import aws_sdk_config_service.types.aggregation_authorization

        out["AggregationAuthorization"] = (
            aws_sdk_config_service.types.aggregation_authorization.serialize_aws_json_1_1(
                value["aggregation_authorization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAggregationAuthorizationResponse:
    out: PutAggregationAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "AggregationAuthorization" in data:
        import aws_sdk_config_service.types.aggregation_authorization

        out["aggregation_authorization"] = (
            aws_sdk_config_service.types.aggregation_authorization.deserialize_aws_json_1_1(
                data["AggregationAuthorization"]
            )
        )
    return out
