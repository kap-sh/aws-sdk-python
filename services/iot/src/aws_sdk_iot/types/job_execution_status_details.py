"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.details_map


class JobExecutionStatusDetails(TypedDict, closed=True):
    details_map: NotRequired["aws_sdk_iot.types.details_map.DetailsMap"]
    """<p>The job execution status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionStatusDetails) -> dict:
    out: dict = {}
    if "details_map" in value:
        import aws_sdk_iot.types.details_map

        out["detailsMap"] = aws_sdk_iot.types.details_map.serialize_json(
            value["details_map"]
        )
    return out


def deserialize_json(data: dict) -> JobExecutionStatusDetails:
    out: JobExecutionStatusDetails = {}  # type: ignore[typeddict-item]
    if "detailsMap" in data:
        import aws_sdk_iot.types.details_map

        out["details_map"] = aws_sdk_iot.types.details_map.deserialize_json(
            data["detailsMap"]
        )
    return out
