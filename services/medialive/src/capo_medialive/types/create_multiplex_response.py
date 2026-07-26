"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.multiplex


class CreateMultiplexResponse(TypedDict, closed=True):
    multiplex: NotRequired["capo_medialive.types.multiplex.Multiplex"]
    """The newly created multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexResponse) -> dict:
    out: dict = {}
    if "multiplex" in value:
        import capo_medialive.types.multiplex

        out["multiplex"] = capo_medialive.types.multiplex.serialize_json(
            value["multiplex"]
        )
    return out


def deserialize_json(data: dict) -> CreateMultiplexResponse:
    out: CreateMultiplexResponse = {}  # type: ignore[typeddict-item]
    if "multiplex" in data:
        import capo_medialive.types.multiplex

        out["multiplex"] = capo_medialive.types.multiplex.deserialize_json(
            data["multiplex"]
        )
    return out
