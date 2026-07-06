"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOutpostOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost


class CreateOutpostOutput(TypedDict, closed=True):
    outpost: NotRequired["aws_sdk_outposts.types.outpost.Outpost"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutpostOutput) -> dict:
    out: dict = {}
    if "outpost" in value:
        import aws_sdk_outposts.types.outpost

        out["Outpost"] = aws_sdk_outposts.types.outpost.serialize_json(value["outpost"])
    return out


def deserialize_json(data: dict) -> CreateOutpostOutput:
    out: CreateOutpostOutput = {}  # type: ignore[typeddict-item]
    if "Outpost" in data:
        import aws_sdk_outposts.types.outpost

        out["outpost"] = aws_sdk_outposts.types.outpost.deserialize_json(
            data["Outpost"]
        )
    return out
