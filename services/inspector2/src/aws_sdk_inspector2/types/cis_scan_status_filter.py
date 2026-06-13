"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatusFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_status
    import aws_sdk_inspector2.types.cis_scan_status_comparison


class CisScanStatusFilter(TypedDict):
    comparison: (
        "aws_sdk_inspector2.types.cis_scan_status_comparison.CisScanStatusComparison"
    )
    """<p>The filter comparison value.</p>"""
    value: "aws_sdk_inspector2.types.cis_scan_status.CisScanStatus"
    """<p>The filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScanStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_scan_status_comparison

    out["comparison"] = (
        aws_sdk_inspector2.types.cis_scan_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import aws_sdk_inspector2.types.cis_scan_status

    out["value"] = aws_sdk_inspector2.types.cis_scan_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisScanStatusFilter:
    out: CisScanStatusFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_scan_status_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_scan_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisScanStatusFilter.comparison required")
    if "value" in data:
        import aws_sdk_inspector2.types.cis_scan_status

        out["value"] = aws_sdk_inspector2.types.cis_scan_status.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisScanStatusFilter.value required")
    return out
