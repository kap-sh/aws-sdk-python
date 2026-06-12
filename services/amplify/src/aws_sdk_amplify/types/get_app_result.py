"""Generated from Smithy shape ``com.amazonaws.amplify#GetAppResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app


class GetAppResult(TypedDict):
    app: "aws_sdk_amplify.types.app.App"


# --- restJson1 ser/de ---
def serialize_json(value: GetAppResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.app

    out["app"] = aws_sdk_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> GetAppResult:
    out: GetAppResult = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_amplify.types.app

        out["app"] = aws_sdk_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("GetAppResult.app required")
    return out
