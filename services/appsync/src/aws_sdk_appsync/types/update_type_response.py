"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.type


class UpdateTypeResponse(TypedDict):
    type: NotRequired["aws_sdk_appsync.types.type.Type"]
    """<p>The updated <code>Type</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTypeResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_appsync.types.type

        out["type"] = aws_sdk_appsync.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UpdateTypeResponse:
    out: UpdateTypeResponse = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_appsync.types.type

        out["type"] = aws_sdk_appsync.types.type.deserialize_json(data["type"])
    return out
