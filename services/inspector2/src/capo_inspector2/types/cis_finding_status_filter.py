"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.cis_finding_status
    import capo_inspector2.types.cis_finding_status_comparison


class CisFindingStatusFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_finding_status_comparison.CisFindingStatusComparison"
    )
    """<p>The comparison value of the CIS finding status filter.</p>"""
    value: "capo_inspector2.types.cis_finding_status.CisFindingStatus"
    """<p>The value of the CIS finding status filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisFindingStatusFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_finding_status_comparison

    out["comparison"] = (
        capo_inspector2.types.cis_finding_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_inspector2.types.cis_finding_status

    out["value"] = capo_inspector2.types.cis_finding_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisFindingStatusFilter:
    out: CisFindingStatusFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import capo_inspector2.types.cis_finding_status_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_finding_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisFindingStatusFilter.comparison required")
    if "value" in data:
        import capo_inspector2.types.cis_finding_status

        out["value"] = capo_inspector2.types.cis_finding_status.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisFindingStatusFilter.value required")
    return out
