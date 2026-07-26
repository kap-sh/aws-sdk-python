"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.session


class GetSessionResponse(TypedDict, closed=True):
    session: "capo_emr_serverless.types.session.Session"
    """<p>The output displays information about the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.session

    out["session"] = capo_emr_serverless.types.session.serialize_json(value["session"])
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "session" in data:
        import capo_emr_serverless.types.session

        out["session"] = capo_emr_serverless.types.session.deserialize_json(
            data["session"]
        )
    else:
        raise DeserializationError("GetSessionResponse.session required")
    return out
