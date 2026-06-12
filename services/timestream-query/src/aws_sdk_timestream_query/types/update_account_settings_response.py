"""Generated from Smithy shape ``com.amazonaws.timestreamquery#UpdateAccountSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.max_query_capacity
    import aws_sdk_timestream_query.types.query_compute_response
    import aws_sdk_timestream_query.types.query_pricing_model


class UpdateAccountSettingsResponse(TypedDict):
    max_query_tcu: NotRequired[
        "aws_sdk_timestream_query.types.max_query_capacity.MaxQueryCapacity"
    ]
    """<p>The configured maximum number of compute units the service will use at any point in time to serve your queries.</p>"""
    query_pricing_model: NotRequired[
        "aws_sdk_timestream_query.types.query_pricing_model.QueryPricingModel"
    ]
    """<p>The pricing model for an account.</p>"""
    query_compute: NotRequired[
        "aws_sdk_timestream_query.types.query_compute_response.QueryComputeResponse"
    ]
    """<p>Confirms the updated account settings for querying data in your account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAccountSettingsResponse) -> dict:
    out: dict = {}
    if "max_query_tcu" in value:
        out["MaxQueryTCU"] = value["max_query_tcu"]
    if "query_pricing_model" in value:
        import aws_sdk_timestream_query.types.query_pricing_model

        out["QueryPricingModel"] = (
            aws_sdk_timestream_query.types.query_pricing_model.serialize_aws_json_1_0(
                value["query_pricing_model"]
            )
        )
    if "query_compute" in value:
        import aws_sdk_timestream_query.types.query_compute_response

        out["QueryCompute"] = (
            aws_sdk_timestream_query.types.query_compute_response.serialize_aws_json_1_0(
                value["query_compute"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAccountSettingsResponse:
    out: UpdateAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "MaxQueryTCU" in data:
        out["max_query_tcu"] = data["MaxQueryTCU"]
    if "QueryPricingModel" in data:
        import aws_sdk_timestream_query.types.query_pricing_model

        out["query_pricing_model"] = (
            aws_sdk_timestream_query.types.query_pricing_model.deserialize_aws_json_1_0(
                data["QueryPricingModel"]
            )
        )
    if "QueryCompute" in data:
        import aws_sdk_timestream_query.types.query_compute_response

        out["query_compute"] = (
            aws_sdk_timestream_query.types.query_compute_response.deserialize_aws_json_1_0(
                data["QueryCompute"]
            )
        )
    return out
