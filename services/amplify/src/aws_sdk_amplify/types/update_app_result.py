"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateAppResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app


class UpdateAppResult(TypedDict, closed=True):
    app: "aws_sdk_amplify.types.app.App"
    """<p>Represents the updated Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.app

    out["app"] = aws_sdk_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> UpdateAppResult:
    out: UpdateAppResult = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_amplify.types.app

        out["app"] = aws_sdk_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("UpdateAppResult.app required")
    return out
