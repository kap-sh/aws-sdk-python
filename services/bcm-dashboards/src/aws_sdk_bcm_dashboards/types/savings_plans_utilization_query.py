"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#SavingsPlansUtilizationQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.date_time_range
    import aws_sdk_bcm_dashboards.types.expression
    import aws_sdk_bcm_dashboards.types.granularity


class SavingsPlansUtilizationQuery(TypedDict):
    time_range: "aws_sdk_bcm_dashboards.types.date_time_range.DateTimeRange"
    granularity: NotRequired["aws_sdk_bcm_dashboards.types.granularity.Granularity"]
    """<p>The time granularity of the retrieved data: <code>HOURLY</code>, <code>DAILY</code>, or <code>MONTHLY</code>.</p>"""
    filter: NotRequired["aws_sdk_bcm_dashboards.types.expression.Expression"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansUtilizationQuery) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.date_time_range

    out["timeRange"] = (
        aws_sdk_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
            value["time_range"]
        )
    )
    if "granularity" in value:
        import aws_sdk_bcm_dashboards.types.granularity

        out["granularity"] = (
            aws_sdk_bcm_dashboards.types.granularity.serialize_aws_json_1_0(
                value["granularity"]
            )
        )
    if "filter" in value:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = aws_sdk_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansUtilizationQuery:
    out: SavingsPlansUtilizationQuery = {}  # type: ignore[typeddict-item]
    if "timeRange" in data:
        import aws_sdk_bcm_dashboards.types.date_time_range

        out["time_range"] = (
            aws_sdk_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    else:
        raise DeserializationError("SavingsPlansUtilizationQuery.time_range required")
    if "granularity" in data:
        import aws_sdk_bcm_dashboards.types.granularity

        out["granularity"] = (
            aws_sdk_bcm_dashboards.types.granularity.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    if "filter" in data:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = (
            aws_sdk_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    return out
