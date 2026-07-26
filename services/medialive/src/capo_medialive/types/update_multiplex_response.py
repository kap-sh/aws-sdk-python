"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateMultiplexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.multiplex


class UpdateMultiplexResponse(TypedDict, closed=True):
    multiplex: NotRequired["capo_medialive.types.multiplex.Multiplex"]
    """The updated multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMultiplexResponse) -> dict:
    out: dict = {}
    if "multiplex" in value:
        import capo_medialive.types.multiplex

        out["multiplex"] = capo_medialive.types.multiplex.serialize_json(
            value["multiplex"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMultiplexResponse:
    out: UpdateMultiplexResponse = {}  # type: ignore[typeddict-item]
    if "multiplex" in data:
        import capo_medialive.types.multiplex

        out["multiplex"] = capo_medialive.types.multiplex.deserialize_json(
            data["multiplex"]
        )
    return out
