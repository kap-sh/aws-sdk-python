"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex


class CreateMultiplexResponse(TypedDict):
    multiplex: NotRequired["aws_sdk_medialive.types.multiplex.Multiplex"]
    """The newly created multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexResponse) -> dict:
    out: dict = {}
    if "multiplex" in value:
        import aws_sdk_medialive.types.multiplex

        out["multiplex"] = aws_sdk_medialive.types.multiplex.serialize_json(
            value["multiplex"]
        )
    return out


def deserialize_json(data: dict) -> CreateMultiplexResponse:
    out: CreateMultiplexResponse = {}  # type: ignore[typeddict-item]
    if "multiplex" in data:
        import aws_sdk_medialive.types.multiplex

        out["multiplex"] = aws_sdk_medialive.types.multiplex.deserialize_json(
            data["multiplex"]
        )
    return out
