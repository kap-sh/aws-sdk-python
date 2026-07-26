"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#PresenterOnlyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.presenter_position


class PresenterOnlyConfiguration(TypedDict, closed=True):
    presenter_position: NotRequired[
        "capo_chime_sdk_media_pipelines.types.presenter_position.PresenterPosition"
    ]
    """<p>Defines the position of the presenter video tile. Default: <code>TopRight</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PresenterOnlyConfiguration) -> dict:
    out: dict = {}
    if "presenter_position" in value:
        import capo_chime_sdk_media_pipelines.types.presenter_position

        out["PresenterPosition"] = (
            capo_chime_sdk_media_pipelines.types.presenter_position.serialize_json(
                value["presenter_position"]
            )
        )
    return out


def deserialize_json(data: dict) -> PresenterOnlyConfiguration:
    out: PresenterOnlyConfiguration = {}  # type: ignore[typeddict-item]
    if "PresenterPosition" in data:
        import capo_chime_sdk_media_pipelines.types.presenter_position

        out["presenter_position"] = (
            capo_chime_sdk_media_pipelines.types.presenter_position.deserialize_json(
                data["PresenterPosition"]
            )
        )
    return out
