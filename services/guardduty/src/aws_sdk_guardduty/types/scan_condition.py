"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.map_equals


class ScanCondition(TypedDict, closed=True):
    map_equals: NotRequired["aws_sdk_guardduty.types.map_equals.MapEquals"]
    """<p>Represents an <i>mapEqual</i> <b/> condition to be applied to a single field when triggering for malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanCondition) -> dict:
    out: dict = {}
    if "map_equals" in value:
        import aws_sdk_guardduty.types.map_equals

        out["mapEquals"] = aws_sdk_guardduty.types.map_equals.serialize_json(
            value["map_equals"]
        )
    return out


def deserialize_json(data: dict) -> ScanCondition:
    out: ScanCondition = {}  # type: ignore[typeddict-item]
    if "mapEquals" in data:
        import aws_sdk_guardduty.types.map_equals

        out["map_equals"] = aws_sdk_guardduty.types.map_equals.deserialize_json(
            data["mapEquals"]
        )
    return out
