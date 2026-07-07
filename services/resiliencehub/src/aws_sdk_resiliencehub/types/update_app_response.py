"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app


class UpdateAppResponse(TypedDict, closed=True):
    app: "aws_sdk_resiliencehub.types.app.App"
    """<p>The specified application, returned as an object with details including compliance status, creation time, description, resiliency score, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.app

    out["app"] = aws_sdk_resiliencehub.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> UpdateAppResponse:
    out: UpdateAppResponse = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import aws_sdk_resiliencehub.types.app

        out["app"] = aws_sdk_resiliencehub.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("UpdateAppResponse.app required")
    return out
