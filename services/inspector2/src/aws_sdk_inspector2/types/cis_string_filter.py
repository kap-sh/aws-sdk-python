"""Generated from Smithy shape ``com.amazonaws.inspector2#CisStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_string_comparison


class CisStringFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.cis_string_comparison.CisStringComparison"
    """<p>The comparison value of the CIS string filter.</p>"""
    value: "str"
    """<p>The value of the CIS string filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisStringFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_string_comparison

    out["comparison"] = aws_sdk_inspector2.types.cis_string_comparison.serialize_json(
        value["comparison"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CisStringFilter:
    out: CisStringFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_string_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_string_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisStringFilter.comparison required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("CisStringFilter.value required")
    return out
