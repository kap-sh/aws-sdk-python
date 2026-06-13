"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_status
    import aws_sdk_inspector2.types.cis_target_status_comparison


class CisTargetStatusFilter(TypedDict):
    comparison: "aws_sdk_inspector2.types.cis_target_status_comparison.CisTargetStatusComparison"
    """<p>The comparison value of the CIS target status filter.</p>"""
    value: "aws_sdk_inspector2.types.cis_target_status.CisTargetStatus"
    """<p>The value of the CIS target status filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_target_status_comparison

    out["comparison"] = (
        aws_sdk_inspector2.types.cis_target_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import aws_sdk_inspector2.types.cis_target_status

    out["value"] = aws_sdk_inspector2.types.cis_target_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisTargetStatusFilter:
    out: CisTargetStatusFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_target_status_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_target_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisTargetStatusFilter.comparison required")
    if "value" in data:
        import aws_sdk_inspector2.types.cis_target_status

        out["value"] = aws_sdk_inspector2.types.cis_target_status.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisTargetStatusFilter.value required")
    return out
