"""Generated from Smithy shape ``com.amazonaws.iot#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.s3_destination


class Destination(TypedDict, closed=True):
    s3_destination: NotRequired["aws_sdk_iot.types.s3_destination.S3Destination"]
    """<p>Describes the location in S3 of the updated firmware.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "s3_destination" in value:
        import aws_sdk_iot.types.s3_destination

        out["s3Destination"] = aws_sdk_iot.types.s3_destination.serialize_json(
            value["s3_destination"]
        )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "s3Destination" in data:
        import aws_sdk_iot.types.s3_destination

        out["s3_destination"] = aws_sdk_iot.types.s3_destination.deserialize_json(
            data["s3Destination"]
        )
    return out
