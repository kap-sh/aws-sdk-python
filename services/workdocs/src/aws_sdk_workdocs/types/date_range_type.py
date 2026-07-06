"""Generated from Smithy shape ``com.amazonaws.workdocs#DateRangeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.timestamp_type


class DateRangeType(TypedDict, closed=True):
    start_value: NotRequired["aws_sdk_workdocs.types.timestamp_type.TimestampType"]
    """<p>Timestamp range start value (in epochs)</p>"""
    end_value: NotRequired["aws_sdk_workdocs.types.timestamp_type.TimestampType"]
    """<p>Timestamp range end value (in epochs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRangeType) -> dict:
    out: dict = {}
    if "start_value" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["StartValue"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["start_value"]
        )
    if "end_value" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["EndValue"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["end_value"]
        )
    return out


def deserialize_json(data: dict) -> DateRangeType:
    out: DateRangeType = {}  # type: ignore[typeddict-item]
    if "StartValue" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["start_value"] = aws_sdk_workdocs.types.timestamp_type.deserialize_json(
            data["StartValue"]
        )
    if "EndValue" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["end_value"] = aws_sdk_workdocs.types.timestamp_type.deserialize_json(
            data["EndValue"]
        )
    return out
