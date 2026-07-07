"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevelFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.cis_security_level_comparison


class CisSecurityLevelFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.cis_security_level_comparison.CisSecurityLevelComparison"
    """<p>The CIS security filter comparison value.</p>"""
    value: "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"
    """<p>The CIS security filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisSecurityLevelFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.cis_security_level_comparison

    out["comparison"] = (
        aws_sdk_inspector2.types.cis_security_level_comparison.serialize_json(
            value["comparison"]
        )
    )
    import aws_sdk_inspector2.types.cis_security_level

    out["value"] = aws_sdk_inspector2.types.cis_security_level.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> CisSecurityLevelFilter:
    out: CisSecurityLevelFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.cis_security_level_comparison

        out["comparison"] = (
            aws_sdk_inspector2.types.cis_security_level_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        raise DeserializationError("CisSecurityLevelFilter.comparison required")
    if "value" in data:
        import aws_sdk_inspector2.types.cis_security_level

        out["value"] = aws_sdk_inspector2.types.cis_security_level.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("CisSecurityLevelFilter.value required")
    return out
