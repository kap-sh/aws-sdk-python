"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateSystemResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.system


class CreateSystemResponse(TypedDict):
    system: "aws_sdk_resiliencehubv2.types.system.System"
    """<p>The created system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSystemResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.system

    out["system"] = aws_sdk_resiliencehubv2.types.system.serialize_json(value["system"])
    return out


def deserialize_json(data: dict) -> CreateSystemResponse:
    out: CreateSystemResponse = {}  # type: ignore[typeddict-item]
    if "system" in data:
        import aws_sdk_resiliencehubv2.types.system

        out["system"] = aws_sdk_resiliencehubv2.types.system.deserialize_json(
            data["system"]
        )
    else:
        raise DeserializationError("CreateSystemResponse.system required")
    return out
