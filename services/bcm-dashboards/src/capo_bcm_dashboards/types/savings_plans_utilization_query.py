"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#SavingsPlansUtilizationQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.date_time_range
    import capo_bcm_dashboards.types.expression
    import capo_bcm_dashboards.types.granularity


class SavingsPlansUtilizationQuery(TypedDict, closed=True):
    time_range: "capo_bcm_dashboards.types.date_time_range.DateTimeRange"
    granularity: NotRequired["capo_bcm_dashboards.types.granularity.Granularity"]
    """<p>The time granularity of the retrieved data: <code>HOURLY</code>, <code>DAILY</code>, or <code>MONTHLY</code>.</p>"""
    filter: NotRequired["capo_bcm_dashboards.types.expression.Expression"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansUtilizationQuery) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.date_time_range

    out["timeRange"] = capo_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
        value["time_range"]
    )
    if "granularity" in value:
        import capo_bcm_dashboards.types.granularity

        out["granularity"] = (
            capo_bcm_dashboards.types.granularity.serialize_aws_json_1_0(
                value["granularity"]
            )
        )
    if "filter" in value:
        import capo_bcm_dashboards.types.expression

        out["filter"] = capo_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansUtilizationQuery:
    out: SavingsPlansUtilizationQuery = {}  # type: ignore[typeddict-item]
    if "timeRange" in data:
        import capo_bcm_dashboards.types.date_time_range

        out["time_range"] = (
            capo_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    else:
        raise DeserializationError("SavingsPlansUtilizationQuery.time_range required")
    if "granularity" in data:
        import capo_bcm_dashboards.types.granularity

        out["granularity"] = (
            capo_bcm_dashboards.types.granularity.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    if "filter" in data:
        import capo_bcm_dashboards.types.expression

        out["filter"] = capo_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
            data["filter"]
        )
    return out
