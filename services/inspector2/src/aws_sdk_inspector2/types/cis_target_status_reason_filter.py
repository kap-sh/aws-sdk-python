"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusReasonFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_status_comparison
    import aws_sdk_inspector2.types.cis_target_status_reason


class CisTargetStatusReasonFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.cis_target_status_comparison.CisTargetStatusComparison"
    """<p>The comparison value of the CIS target status reason filter.</p>"""
    value: "aws_sdk_inspector2.types.cis_target_status_reason.CisTargetStatusReason"
    """<p>The value of the CIS target status reason filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusReasonFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_target_status_comparison

    out["comparison"] = (
        aws_sdk_inspector2.types.cis_target_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import aws_sdk_inspector2.types.cis_target_status_reason

    out["value"] = aws_sdk_inspector2.types.cis_target_status_reason.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisTargetStatusReasonFilter:
    out: CisTargetStatusReasonFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_target_status_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_target_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisTargetStatusReasonFilter.comparison required")
    if "value" in data:
        import aws_sdk_inspector2.types.cis_target_status_reason

        out["value"] = (
            aws_sdk_inspector2.types.cis_target_status_reason.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("CisTargetStatusReasonFilter.value required")
    return out
