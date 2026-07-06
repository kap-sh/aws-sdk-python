"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.tapes


class DescribeTapesOutput(TypedDict, closed=True):
    tapes: NotRequired["aws_sdk_storage_gateway.types.tapes.Tapes"]
    """<p>An array of virtual tape descriptions.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that can be used as part of a subsequent <code>DescribeTapes</code> call to retrieve the next page of results.</p> <p>If a response does not contain a marker, then there are no more results to be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapesOutput) -> dict:
    out: dict = {}
    if "tapes" in value:
        import aws_sdk_storage_gateway.types.tapes

        out["Tapes"] = aws_sdk_storage_gateway.types.tapes.serialize_aws_json_1_1(
            value["tapes"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapesOutput:
    out: DescribeTapesOutput = {}  # type: ignore[typeddict-item]
    if "Tapes" in data:
        import aws_sdk_storage_gateway.types.tapes

        out["tapes"] = aws_sdk_storage_gateway.types.tapes.deserialize_aws_json_1_1(
            data["Tapes"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
