"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetApproximateUsageRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.approximation_dimension
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.usage_services


class GetApproximateUsageRecordsRequest(TypedDict, closed=True):
    granularity: "capo_cost_explorer.types.granularity.Granularity"
    """<p>How granular you want the data to be. You can enable data at hourly or daily granularity.</p>"""
    services: NotRequired["capo_cost_explorer.types.usage_services.UsageServices"]
    """<p>The service metadata for the service or services you want to query. If not specified, all elements are returned.</p>"""
    approximation_dimension: (
        "capo_cost_explorer.types.approximation_dimension.ApproximationDimension"
    )
    """<p>The service to evaluate for the usage records. You can choose resource-level data at daily granularity, or hourly granularity with or without resource-level data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApproximateUsageRecordsRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.granularity

    out["Granularity"] = capo_cost_explorer.types.granularity.serialize_aws_json_1_1(
        value["granularity"]
    )
    if "services" in value:
        import capo_cost_explorer.types.usage_services

        out["Services"] = (
            capo_cost_explorer.types.usage_services.serialize_aws_json_1_1(
                value["services"]
            )
        )
    import capo_cost_explorer.types.approximation_dimension

    out["ApproximationDimension"] = (
        capo_cost_explorer.types.approximation_dimension.serialize_aws_json_1_1(
            value["approximation_dimension"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApproximateUsageRecordsRequest:
    out: GetApproximateUsageRecordsRequest = {}  # type: ignore[typeddict-item]
    if "Granularity" in data:
        import capo_cost_explorer.types.granularity

        out["granularity"] = (
            capo_cost_explorer.types.granularity.deserialize_aws_json_1_1(
                data["Granularity"]
            )
        )
    else:
        raise DeserializationError(
            "GetApproximateUsageRecordsRequest.granularity required"
        )
    if "Services" in data:
        import capo_cost_explorer.types.usage_services

        out["services"] = (
            capo_cost_explorer.types.usage_services.deserialize_aws_json_1_1(
                data["Services"]
            )
        )
    if "ApproximationDimension" in data:
        import capo_cost_explorer.types.approximation_dimension

        out["approximation_dimension"] = (
            capo_cost_explorer.types.approximation_dimension.deserialize_aws_json_1_1(
                data["ApproximationDimension"]
            )
        )
    else:
        raise DeserializationError(
            "GetApproximateUsageRecordsRequest.approximation_dimension required"
        )
    return out
