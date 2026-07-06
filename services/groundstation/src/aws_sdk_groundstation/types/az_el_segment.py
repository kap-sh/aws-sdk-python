"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.iso8601_time_range
    import aws_sdk_groundstation.types.time_az_el_list


class AzElSegment(TypedDict, closed=True):
    reference_epoch: "datetime.datetime"
    """<p>The reference time for this segment in ISO 8601 format in Coordinated Universal Time (UTC).</p> <p>All time values within the segment's <a>AzElSegment$azElList</a> are specified as offsets in atomic seconds from this reference epoch.</p> <p>Example: <code>2024-01-15T12:00:00.000Z</code> </p>"""
    valid_time_range: "aws_sdk_groundstation.types.iso8601_time_range.ISO8601TimeRange"
    """<p>The valid time range for this segment.</p> <p> Specifies the start and end timestamps in ISO 8601 format in Coordinated Universal Time (UTC). The segment's pointing data must cover this entire time range. </p>"""
    az_el_list: "aws_sdk_groundstation.types.time_az_el_list.TimeAzElList"
    """<p>List of time-tagged azimuth elevation data points.</p> <p> Must contain at least five points to support 4th order Lagrange interpolation. Points must be in chronological order with no duplicates. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegment) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types._prelude.timestamp

    out["referenceEpoch"] = (
        aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
            value["reference_epoch"]
        )
    )
    import aws_sdk_groundstation.types.iso8601_time_range

    out["validTimeRange"] = (
        aws_sdk_groundstation.types.iso8601_time_range.serialize_json(
            value["valid_time_range"]
        )
    )
    import aws_sdk_groundstation.types.time_az_el_list

    out["azElList"] = aws_sdk_groundstation.types.time_az_el_list.serialize_json(
        value["az_el_list"]
    )
    return out


def deserialize_json(data: dict) -> AzElSegment:
    out: AzElSegment = {}  # type: ignore[typeddict-item]
    if "referenceEpoch" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["reference_epoch"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["referenceEpoch"]
            )
        )
    else:
        raise DeserializationError("AzElSegment.reference_epoch required")
    if "validTimeRange" in data:
        import aws_sdk_groundstation.types.iso8601_time_range

        out["valid_time_range"] = (
            aws_sdk_groundstation.types.iso8601_time_range.deserialize_json(
                data["validTimeRange"]
            )
        )
    else:
        raise DeserializationError("AzElSegment.valid_time_range required")
    if "azElList" in data:
        import aws_sdk_groundstation.types.time_az_el_list

        out["az_el_list"] = (
            aws_sdk_groundstation.types.time_az_el_list.deserialize_json(
                data["azElList"]
            )
        )
    else:
        raise DeserializationError("AzElSegment.az_el_list required")
    return out
