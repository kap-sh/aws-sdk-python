"""Generated from Smithy shape ``com.amazonaws.costexplorer#Coverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.coverage_cost
    import capo_cost_explorer.types.coverage_hours
    import capo_cost_explorer.types.coverage_normalized_units


class Coverage(TypedDict, closed=True):
    coverage_hours: NotRequired["capo_cost_explorer.types.coverage_hours.CoverageHours"]
    """<p>The amount of instance usage that the reservation covered, in hours.</p>"""
    coverage_normalized_units: NotRequired[
        "capo_cost_explorer.types.coverage_normalized_units.CoverageNormalizedUnits"
    ]
    """<p>The amount of instance usage that the reservation covered, in normalized units.</p>"""
    coverage_cost: NotRequired["capo_cost_explorer.types.coverage_cost.CoverageCost"]
    """<p>The amount of cost that the reservation covered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Coverage) -> dict:
    out: dict = {}
    if "coverage_hours" in value:
        import capo_cost_explorer.types.coverage_hours

        out["CoverageHours"] = (
            capo_cost_explorer.types.coverage_hours.serialize_aws_json_1_1(
                value["coverage_hours"]
            )
        )
    if "coverage_normalized_units" in value:
        import capo_cost_explorer.types.coverage_normalized_units

        out["CoverageNormalizedUnits"] = (
            capo_cost_explorer.types.coverage_normalized_units.serialize_aws_json_1_1(
                value["coverage_normalized_units"]
            )
        )
    if "coverage_cost" in value:
        import capo_cost_explorer.types.coverage_cost

        out["CoverageCost"] = (
            capo_cost_explorer.types.coverage_cost.serialize_aws_json_1_1(
                value["coverage_cost"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Coverage:
    out: Coverage = {}  # type: ignore[typeddict-item]
    if "CoverageHours" in data:
        import capo_cost_explorer.types.coverage_hours

        out["coverage_hours"] = (
            capo_cost_explorer.types.coverage_hours.deserialize_aws_json_1_1(
                data["CoverageHours"]
            )
        )
    if "CoverageNormalizedUnits" in data:
        import capo_cost_explorer.types.coverage_normalized_units

        out["coverage_normalized_units"] = (
            capo_cost_explorer.types.coverage_normalized_units.deserialize_aws_json_1_1(
                data["CoverageNormalizedUnits"]
            )
        )
    if "CoverageCost" in data:
        import capo_cost_explorer.types.coverage_cost

        out["coverage_cost"] = (
            capo_cost_explorer.types.coverage_cost.deserialize_aws_json_1_1(
                data["CoverageCost"]
            )
        )
    return out
