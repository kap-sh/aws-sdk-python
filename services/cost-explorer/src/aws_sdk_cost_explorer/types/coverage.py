"""Generated from Smithy shape ``com.amazonaws.costexplorer#Coverage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.coverage_cost
    import aws_sdk_cost_explorer.types.coverage_hours
    import aws_sdk_cost_explorer.types.coverage_normalized_units


class Coverage(TypedDict):
    coverage_hours: NotRequired[
        "aws_sdk_cost_explorer.types.coverage_hours.CoverageHours"
    ]
    """<p>The amount of instance usage that the reservation covered, in hours.</p>"""
    coverage_normalized_units: NotRequired[
        "aws_sdk_cost_explorer.types.coverage_normalized_units.CoverageNormalizedUnits"
    ]
    """<p>The amount of instance usage that the reservation covered, in normalized units.</p>"""
    coverage_cost: NotRequired["aws_sdk_cost_explorer.types.coverage_cost.CoverageCost"]
    """<p>The amount of cost that the reservation covered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Coverage) -> dict:
    out: dict = {}
    if "coverage_hours" in value:
        import aws_sdk_cost_explorer.types.coverage_hours

        out["CoverageHours"] = (
            aws_sdk_cost_explorer.types.coverage_hours.serialize_aws_json_1_1(
                value["coverage_hours"]
            )
        )
    if "coverage_normalized_units" in value:
        import aws_sdk_cost_explorer.types.coverage_normalized_units

        out["CoverageNormalizedUnits"] = (
            aws_sdk_cost_explorer.types.coverage_normalized_units.serialize_aws_json_1_1(
                value["coverage_normalized_units"]
            )
        )
    if "coverage_cost" in value:
        import aws_sdk_cost_explorer.types.coverage_cost

        out["CoverageCost"] = (
            aws_sdk_cost_explorer.types.coverage_cost.serialize_aws_json_1_1(
                value["coverage_cost"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Coverage:
    out: Coverage = {}  # type: ignore[typeddict-item]
    if "CoverageHours" in data:
        import aws_sdk_cost_explorer.types.coverage_hours

        out["coverage_hours"] = (
            aws_sdk_cost_explorer.types.coverage_hours.deserialize_aws_json_1_1(
                data["CoverageHours"]
            )
        )
    if "CoverageNormalizedUnits" in data:
        import aws_sdk_cost_explorer.types.coverage_normalized_units

        out["coverage_normalized_units"] = (
            aws_sdk_cost_explorer.types.coverage_normalized_units.deserialize_aws_json_1_1(
                data["CoverageNormalizedUnits"]
            )
        )
    if "CoverageCost" in data:
        import aws_sdk_cost_explorer.types.coverage_cost

        out["coverage_cost"] = (
            aws_sdk_cost_explorer.types.coverage_cost.deserialize_aws_json_1_1(
                data["CoverageCost"]
            )
        )
    return out
