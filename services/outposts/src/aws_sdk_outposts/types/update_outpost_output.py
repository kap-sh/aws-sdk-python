"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateOutpostOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost


class UpdateOutpostOutput(TypedDict):
    outpost: NotRequired["aws_sdk_outposts.types.outpost.Outpost"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutpostOutput) -> dict:
    out: dict = {}
    if "outpost" in value:
        import aws_sdk_outposts.types.outpost

        out["Outpost"] = aws_sdk_outposts.types.outpost.serialize_json(value["outpost"])
    return out


def deserialize_json(data: dict) -> UpdateOutpostOutput:
    out: UpdateOutpostOutput = {}  # type: ignore[typeddict-item]
    if "Outpost" in data:
        import aws_sdk_outposts.types.outpost

        out["outpost"] = aws_sdk_outposts.types.outpost.deserialize_json(
            data["Outpost"]
        )
    return out
