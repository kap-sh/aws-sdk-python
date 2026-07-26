"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_state
    import capo_iotsitewise.types.error_details


class AssetStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.asset_state.AssetState"
    """<p>The current status of the asset.</p>"""
    error: NotRequired["capo_iotsitewise.types.error_details.ErrorDetails"]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_state

    out["state"] = capo_iotsitewise.types.asset_state.serialize_json(value["state"])
    if "error" in value:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AssetStatus:
    out: AssetStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_iotsitewise.types.asset_state

        out["state"] = capo_iotsitewise.types.asset_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("AssetStatus.state required")
    if "error" in data:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
