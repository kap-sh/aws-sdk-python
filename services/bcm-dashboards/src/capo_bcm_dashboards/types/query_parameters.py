"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#QueryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.cost_and_usage_query
    import capo_bcm_dashboards.types.reservation_coverage_query
    import capo_bcm_dashboards.types.reservation_utilization_query
    import capo_bcm_dashboards.types.savings_plans_coverage_query
    import capo_bcm_dashboards.types.savings_plans_utilization_query


class _QueryParameters_costAndUsage(TypedDict, closed=True):
    costAndUsage: "capo_bcm_dashboards.types.cost_and_usage_query.CostAndUsageQuery"


class _QueryParameters_savingsPlansCoverage(TypedDict, closed=True):
    savingsPlansCoverage: "capo_bcm_dashboards.types.savings_plans_coverage_query.SavingsPlansCoverageQuery"


class _QueryParameters_savingsPlansUtilization(TypedDict, closed=True):
    savingsPlansUtilization: "capo_bcm_dashboards.types.savings_plans_utilization_query.SavingsPlansUtilizationQuery"


class _QueryParameters_reservationCoverage(TypedDict, closed=True):
    reservationCoverage: (
        "capo_bcm_dashboards.types.reservation_coverage_query.ReservationCoverageQuery"
    )


class _QueryParameters_reservationUtilization(TypedDict, closed=True):
    reservationUtilization: "capo_bcm_dashboards.types.reservation_utilization_query.ReservationUtilizationQuery"


QueryParameters: TypeAlias = (
    _QueryParameters_costAndUsage
    | _QueryParameters_savingsPlansCoverage
    | _QueryParameters_savingsPlansUtilization
    | _QueryParameters_reservationCoverage
    | _QueryParameters_reservationUtilization
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryParameters) -> dict:
    if "costAndUsage" in value:
        import capo_bcm_dashboards.types.cost_and_usage_query

        return {
            "costAndUsage": capo_bcm_dashboards.types.cost_and_usage_query.serialize_aws_json_1_0(
                value["costAndUsage"]
            )
        }
    elif "savingsPlansCoverage" in value:
        import capo_bcm_dashboards.types.savings_plans_coverage_query

        return {
            "savingsPlansCoverage": capo_bcm_dashboards.types.savings_plans_coverage_query.serialize_aws_json_1_0(
                value["savingsPlansCoverage"]
            )
        }
    elif "savingsPlansUtilization" in value:
        import capo_bcm_dashboards.types.savings_plans_utilization_query

        return {
            "savingsPlansUtilization": capo_bcm_dashboards.types.savings_plans_utilization_query.serialize_aws_json_1_0(
                value["savingsPlansUtilization"]
            )
        }
    elif "reservationCoverage" in value:
        import capo_bcm_dashboards.types.reservation_coverage_query

        return {
            "reservationCoverage": capo_bcm_dashboards.types.reservation_coverage_query.serialize_aws_json_1_0(
                value["reservationCoverage"]
            )
        }
    elif "reservationUtilization" in value:
        import capo_bcm_dashboards.types.reservation_utilization_query

        return {
            "reservationUtilization": capo_bcm_dashboards.types.reservation_utilization_query.serialize_aws_json_1_0(
                value["reservationUtilization"]
            )
        }
    else:
        raise SerializationError("QueryParameters: no variant present")


def deserialize_aws_json_1_0(data: dict) -> QueryParameters:
    if "costAndUsage" in data:
        import capo_bcm_dashboards.types.cost_and_usage_query

        return {
            "costAndUsage": capo_bcm_dashboards.types.cost_and_usage_query.deserialize_aws_json_1_0(
                data["costAndUsage"]
            )
        }
    elif "savingsPlansCoverage" in data:
        import capo_bcm_dashboards.types.savings_plans_coverage_query

        return {
            "savingsPlansCoverage": capo_bcm_dashboards.types.savings_plans_coverage_query.deserialize_aws_json_1_0(
                data["savingsPlansCoverage"]
            )
        }
    elif "savingsPlansUtilization" in data:
        import capo_bcm_dashboards.types.savings_plans_utilization_query

        return {
            "savingsPlansUtilization": capo_bcm_dashboards.types.savings_plans_utilization_query.deserialize_aws_json_1_0(
                data["savingsPlansUtilization"]
            )
        }
    elif "reservationCoverage" in data:
        import capo_bcm_dashboards.types.reservation_coverage_query

        return {
            "reservationCoverage": capo_bcm_dashboards.types.reservation_coverage_query.deserialize_aws_json_1_0(
                data["reservationCoverage"]
            )
        }
    elif "reservationUtilization" in data:
        import capo_bcm_dashboards.types.reservation_utilization_query

        return {
            "reservationUtilization": capo_bcm_dashboards.types.reservation_utilization_query.deserialize_aws_json_1_0(
                data["reservationUtilization"]
            )
        }
    else:
        raise DeserializationError("QueryParameters: no recognized variant key")
