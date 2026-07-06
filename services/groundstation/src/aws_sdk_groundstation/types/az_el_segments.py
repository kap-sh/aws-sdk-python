"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegments``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.angle_units
    import aws_sdk_groundstation.types.az_el_segment_list


class AzElSegments(TypedDict, closed=True):
    angle_unit: "aws_sdk_groundstation.types.angle_units.AngleUnits"
    """<p>The unit of measure for azimuth and elevation angles. All angles in all segments must use the same unit.</p>"""
    az_el_segment_list: "aws_sdk_groundstation.types.az_el_segment_list.AzElSegmentList"
    """<p>List of azimuth elevation segments.</p> <p>Must contain between 1 and 100 segments. Segments must be in chronological order with no overlaps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegments) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.angle_units

    out["angleUnit"] = aws_sdk_groundstation.types.angle_units.serialize_json(
        value["angle_unit"]
    )
    import aws_sdk_groundstation.types.az_el_segment_list

    out["azElSegmentList"] = (
        aws_sdk_groundstation.types.az_el_segment_list.serialize_json(
            value["az_el_segment_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> AzElSegments:
    out: AzElSegments = {}  # type: ignore[typeddict-item]
    if "angleUnit" in data:
        import aws_sdk_groundstation.types.angle_units

        out["angle_unit"] = aws_sdk_groundstation.types.angle_units.deserialize_json(
            data["angleUnit"]
        )
    else:
        raise DeserializationError("AzElSegments.angle_unit required")
    if "azElSegmentList" in data:
        import aws_sdk_groundstation.types.az_el_segment_list

        out["az_el_segment_list"] = (
            aws_sdk_groundstation.types.az_el_segment_list.deserialize_json(
                data["azElSegmentList"]
            )
        )
    else:
        raise DeserializationError("AzElSegments.az_el_segment_list required")
    return out
