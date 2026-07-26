"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.cis_target_status
    import capo_inspector2.types.cis_target_status_comparison


class CisTargetStatusFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.cis_target_status_comparison.CisTargetStatusComparison"
    )
    """<p>The comparison value of the CIS target status filter.</p>"""
    value: "capo_inspector2.types.cis_target_status.CisTargetStatus"
    """<p>The value of the CIS target status filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.cis_target_status_comparison

    out["comparison"] = (
        capo_inspector2.types.cis_target_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import capo_inspector2.types.cis_target_status

    out["value"] = capo_inspector2.types.cis_target_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisTargetStatusFilter:
    out: CisTargetStatusFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import capo_inspector2.types.cis_target_status_comparison

        out["comparison"] = (
            capo_inspector2.types.cis_target_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisTargetStatusFilter.comparison required")
    if "value" in data:
        import capo_inspector2.types.cis_target_status

        out["value"] = capo_inspector2.types.cis_target_status.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisTargetStatusFilter.value required")
    return out
