"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationCoverageGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.attributes
    import capo_cost_explorer.types.coverage


class ReservationCoverageGroup(TypedDict, closed=True):
    attributes: NotRequired["capo_cost_explorer.types.attributes.Attributes"]
    """<p>The attributes for this group of reservations.</p>"""
    coverage: NotRequired["capo_cost_explorer.types.coverage.Coverage"]
    """<p>How much instance usage this group of reservations covered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationCoverageGroup) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_cost_explorer.types.attributes

        out["Attributes"] = capo_cost_explorer.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "coverage" in value:
        import capo_cost_explorer.types.coverage

        out["Coverage"] = capo_cost_explorer.types.coverage.serialize_aws_json_1_1(
            value["coverage"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationCoverageGroup:
    out: ReservationCoverageGroup = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_cost_explorer.types.attributes

        out["attributes"] = (
            capo_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Coverage" in data:
        import capo_cost_explorer.types.coverage

        out["coverage"] = capo_cost_explorer.types.coverage.deserialize_aws_json_1_1(
            data["Coverage"]
        )
    return out
