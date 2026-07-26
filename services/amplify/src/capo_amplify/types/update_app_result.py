"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateAppResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.app


class UpdateAppResult(TypedDict, closed=True):
    app: "capo_amplify.types.app.App"
    """<p>Represents the updated Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppResult) -> dict:
    out: dict = {}
    import capo_amplify.types.app

    out["app"] = capo_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> UpdateAppResult:
    out: UpdateAppResult = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import capo_amplify.types.app

        out["app"] = capo_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("UpdateAppResult.app required")
    return out
