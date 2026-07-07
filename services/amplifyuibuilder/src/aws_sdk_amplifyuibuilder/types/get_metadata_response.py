"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.features_map


class GetMetadataResponse(TypedDict, closed=True):
    features: "aws_sdk_amplifyuibuilder.types.features_map.FeaturesMap"
    """<p>Represents the configuration settings for the features metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataResponse) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.features_map

    out["features"] = aws_sdk_amplifyuibuilder.types.features_map.serialize_json(
        value["features"]
    )
    return out


def deserialize_json(data: dict) -> GetMetadataResponse:
    out: GetMetadataResponse = {}  # type: ignore[typeddict-item]
    if "features" in data:
        import aws_sdk_amplifyuibuilder.types.features_map

        out["features"] = aws_sdk_amplifyuibuilder.types.features_map.deserialize_json(
            data["features"]
        )
    else:
        raise DeserializationError("GetMetadataResponse.features required")
    return out
