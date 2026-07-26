"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateApiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.api


class UpdateApiResponse(TypedDict, closed=True):
    api: NotRequired["capo_appsync.types.api.Api"]
    """<p>The <code>Api</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiResponse) -> dict:
    out: dict = {}
    if "api" in value:
        import capo_appsync.types.api

        out["api"] = capo_appsync.types.api.serialize_json(value["api"])
    return out


def deserialize_json(data: dict) -> UpdateApiResponse:
    out: UpdateApiResponse = {}  # type: ignore[typeddict-item]
    if "api" in data:
        import capo_appsync.types.api

        out["api"] = capo_appsync.types.api.deserialize_json(data["api"])
    return out
