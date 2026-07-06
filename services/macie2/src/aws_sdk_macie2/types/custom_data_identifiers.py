"""Generated from Smithy shape ``com.amazonaws.macie2#CustomDataIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.custom_detections


class CustomDataIdentifiers(TypedDict, closed=True):
    detections: NotRequired["aws_sdk_macie2.types.custom_detections.CustomDetections"]
    """<p>The custom data identifiers that detected the data, and the number of occurrences of the data that each identifier detected.</p>"""
    total_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the data that was detected by the custom data identifiers and produced the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifiers) -> dict:
    out: dict = {}
    if "detections" in value:
        import aws_sdk_macie2.types.custom_detections

        out["detections"] = aws_sdk_macie2.types.custom_detections.serialize_json(
            value["detections"]
        )
    if "total_count" in value:
        out["totalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> CustomDataIdentifiers:
    out: CustomDataIdentifiers = {}  # type: ignore[typeddict-item]
    if "detections" in data:
        import aws_sdk_macie2.types.custom_detections

        out["detections"] = aws_sdk_macie2.types.custom_detections.deserialize_json(
            data["detections"]
        )
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    return out
