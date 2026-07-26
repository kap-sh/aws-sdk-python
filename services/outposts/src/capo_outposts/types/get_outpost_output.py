"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.outpost


class GetOutpostOutput(TypedDict, closed=True):
    outpost: NotRequired["capo_outposts.types.outpost.Outpost"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostOutput) -> dict:
    out: dict = {}
    if "outpost" in value:
        import capo_outposts.types.outpost

        out["Outpost"] = capo_outposts.types.outpost.serialize_json(value["outpost"])
    return out


def deserialize_json(data: dict) -> GetOutpostOutput:
    out: GetOutpostOutput = {}  # type: ignore[typeddict-item]
    if "Outpost" in data:
        import capo_outposts.types.outpost

        out["outpost"] = capo_outposts.types.outpost.deserialize_json(data["Outpost"])
    return out
