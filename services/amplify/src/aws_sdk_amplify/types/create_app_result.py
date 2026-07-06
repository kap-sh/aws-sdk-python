"""Generated from Smithy shape ``com.amazonaws.amplify#CreateAppResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app


class CreateAppResult(TypedDict, closed=True):
    app: "aws_sdk_amplify.types.app.App"


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.app

    out["app"] = aws_sdk_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> CreateAppResult:
    out: CreateAppResult = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_amplify.types.app

        out["app"] = aws_sdk_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("CreateAppResult.app required")
    return out
