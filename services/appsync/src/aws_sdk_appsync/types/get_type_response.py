"""Generated from Smithy shape ``com.amazonaws.appsync#GetTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.type


class GetTypeResponse(TypedDict):
    type: NotRequired["aws_sdk_appsync.types.type.Type"]
    """<p>The <code>Type</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTypeResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_appsync.types.type

        out["type"] = aws_sdk_appsync.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> GetTypeResponse:
    out: GetTypeResponse = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_appsync.types.type

        out["type"] = aws_sdk_appsync.types.type.deserialize_json(data["type"])
    return out
