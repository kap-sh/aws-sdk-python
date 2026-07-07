"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageAdditionalDestinations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.output_location_ref


class MediaPackageAdditionalDestinations(TypedDict, closed=True):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """The destination location"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageAdditionalDestinations) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> MediaPackageAdditionalDestinations:
    out: MediaPackageAdditionalDestinations = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    return out
