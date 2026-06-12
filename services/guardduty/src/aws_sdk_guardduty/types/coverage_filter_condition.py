"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageFilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.equals
    import aws_sdk_guardduty.types.not_equals


class CoverageFilterCondition(TypedDict):
    equals: NotRequired["aws_sdk_guardduty.types.equals.Equals"]
    """<p>Represents an equal condition that is applied to a single field while retrieving the coverage details.</p>"""
    not_equals: NotRequired["aws_sdk_guardduty.types.not_equals.NotEquals"]
    """<p>Represents a not equal condition that is applied to a single field while retrieving the coverage details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCondition) -> dict:
    out: dict = {}
    if "equals" in value:
        import aws_sdk_guardduty.types.equals

        out["equals"] = aws_sdk_guardduty.types.equals.serialize_json(value["equals"])
    if "not_equals" in value:
        import aws_sdk_guardduty.types.not_equals

        out["notEquals"] = aws_sdk_guardduty.types.not_equals.serialize_json(
            value["not_equals"]
        )
    return out


def deserialize_json(data: dict) -> CoverageFilterCondition:
    out: CoverageFilterCondition = {}  # type: ignore[typeddict-item]
    if "equals" in data:
        import aws_sdk_guardduty.types.equals

        out["equals"] = aws_sdk_guardduty.types.equals.deserialize_json(data["equals"])
    if "notEquals" in data:
        import aws_sdk_guardduty.types.not_equals

        out["not_equals"] = aws_sdk_guardduty.types.not_equals.deserialize_json(
            data["notEquals"]
        )
    return out
