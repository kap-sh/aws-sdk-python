"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#LayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.grid_configuration
    import capo_ivs_realtime.types.pip_configuration


class LayoutConfiguration(TypedDict, closed=True):
    grid: NotRequired["capo_ivs_realtime.types.grid_configuration.GridConfiguration"]
    """<p>Configuration related to grid layout. Default: Grid layout.</p>"""
    pip: NotRequired["capo_ivs_realtime.types.pip_configuration.PipConfiguration"]
    """<p>Configuration related to PiP layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutConfiguration) -> dict:
    out: dict = {}
    if "grid" in value:
        import capo_ivs_realtime.types.grid_configuration

        out["grid"] = capo_ivs_realtime.types.grid_configuration.serialize_json(
            value["grid"]
        )
    if "pip" in value:
        import capo_ivs_realtime.types.pip_configuration

        out["pip"] = capo_ivs_realtime.types.pip_configuration.serialize_json(
            value["pip"]
        )
    return out


def deserialize_json(data: dict) -> LayoutConfiguration:
    out: LayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "grid" in data:
        import capo_ivs_realtime.types.grid_configuration

        out["grid"] = capo_ivs_realtime.types.grid_configuration.deserialize_json(
            data["grid"]
        )
    if "pip" in data:
        import capo_ivs_realtime.types.pip_configuration

        out["pip"] = capo_ivs_realtime.types.pip_configuration.deserialize_json(
            data["pip"]
        )
    return out
