"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteAppResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app


class DeleteAppResult(TypedDict, closed=True):
    app: "aws_sdk_amplify.types.app.App"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.app

    out["app"] = aws_sdk_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> DeleteAppResult:
    out: DeleteAppResult = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_amplify.types.app

        out["app"] = aws_sdk_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("DeleteAppResult.app required")
    return out
