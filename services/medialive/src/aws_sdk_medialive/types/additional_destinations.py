"""Generated from Smithy shape ``com.amazonaws.medialive#AdditionalDestinations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.output_location_ref


class AdditionalDestinations(TypedDict):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """The destination location"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalDestinations) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> AdditionalDestinations:
    out: AdditionalDestinations = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    return out
