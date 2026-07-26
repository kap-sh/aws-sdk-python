"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string


class DeleteSessionRequest(TypedDict, closed=True):
    id: "capo_glue.types.name_string.NameString"
    """<p>The ID of the session to be deleted.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The name of the origin of the delete session request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSessionRequest:
    out: DeleteSessionRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteSessionRequest.id required")
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
