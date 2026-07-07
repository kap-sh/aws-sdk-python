"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_result_status
    import aws_sdk_inspector2.types.cis_result_status_comparison


class CisResultStatusFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.cis_result_status_comparison.CisResultStatusComparison"
    """<p>The comparison value of the CIS result status filter.</p>"""
    value: "aws_sdk_inspector2.types.cis_result_status.CisResultStatus"
    """<p>The value of the CIS result status filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_result_status_comparison

    out["comparison"] = (
        aws_sdk_inspector2.types.cis_result_status_comparison.serialize_json(
            value["comparison"]
        )
    )
    import aws_sdk_inspector2.types.cis_result_status

    out["value"] = aws_sdk_inspector2.types.cis_result_status.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisResultStatusFilter:
    out: CisResultStatusFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_result_status_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_result_status_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisResultStatusFilter.comparison required")
    if "value" in data:
        import aws_sdk_inspector2.types.cis_result_status

        out["value"] = aws_sdk_inspector2.types.cis_result_status.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisResultStatusFilter.value required")
    return out
