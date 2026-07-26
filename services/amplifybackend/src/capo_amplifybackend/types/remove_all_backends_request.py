"""Generated from Smithy shape ``com.amazonaws.amplifybackend#RemoveAllBackendsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__boolean
    import capo_amplifybackend.types.__string


class RemoveAllBackendsRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    clean_amplify_app: NotRequired["capo_amplifybackend.types.__boolean.__boolean"]
    """<p>Cleans up the Amplify Console app if this value is set to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAllBackendsRequest) -> dict:
    out: dict = {}
    if "clean_amplify_app" in value:
        out["cleanAmplifyApp"] = value["clean_amplify_app"]
    return out


def deserialize_json(data: dict) -> RemoveAllBackendsRequest:
    out: RemoveAllBackendsRequest = {}  # type: ignore[typeddict-item]
    if "cleanAmplifyApp" in data:
        out["clean_amplify_app"] = data["cleanAmplifyApp"]
    return out
