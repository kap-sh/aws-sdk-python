"""Generated from Smithy shape ``com.amazonaws.iot#GetPercentilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.percentiles


class GetPercentilesResponse(TypedDict, closed=True):
    percentiles: NotRequired["aws_sdk_iot.types.percentiles.Percentiles"]
    """<p>The percentile values of the aggregated fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPercentilesResponse) -> dict:
    out: dict = {}
    if "percentiles" in value:
        import aws_sdk_iot.types.percentiles

        out["percentiles"] = aws_sdk_iot.types.percentiles.serialize_json(
            value["percentiles"]
        )
    return out


def deserialize_json(data: dict) -> GetPercentilesResponse:
    out: GetPercentilesResponse = {}  # type: ignore[typeddict-item]
    if "percentiles" in data:
        import aws_sdk_iot.types.percentiles

        out["percentiles"] = aws_sdk_iot.types.percentiles.deserialize_json(
            data["percentiles"]
        )
    return out
