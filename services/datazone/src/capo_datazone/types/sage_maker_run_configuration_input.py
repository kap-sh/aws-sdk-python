"""Generated from Smithy shape ``com.amazonaws.datazone#SageMakerRunConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.tracking_assets


class SageMakerRunConfigurationInput(TypedDict, closed=True):
    tracking_assets: "capo_datazone.types.tracking_assets.TrackingAssets"
    """<p>The tracking assets of the Amazon SageMaker run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerRunConfigurationInput) -> dict:
    out: dict = {}
    import capo_datazone.types.tracking_assets

    out["trackingAssets"] = capo_datazone.types.tracking_assets.serialize_json(
        value["tracking_assets"]
    )
    return out


def deserialize_json(data: dict) -> SageMakerRunConfigurationInput:
    out: SageMakerRunConfigurationInput = {}  # type: ignore[typeddict-item]
    if "trackingAssets" in data:
        import capo_datazone.types.tracking_assets

        out["tracking_assets"] = capo_datazone.types.tracking_assets.deserialize_json(
            data["trackingAssets"]
        )
    else:
        raise DeserializationError(
            "SageMakerRunConfigurationInput.tracking_assets required"
        )
    return out
