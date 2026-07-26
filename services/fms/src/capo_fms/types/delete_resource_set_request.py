"""Generated from Smithy shape ``com.amazonaws.fms#DeleteResourceSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.base62_id


class DeleteResourceSetRequest(TypedDict, closed=True):
    identifier: "capo_fms.types.base62_id.Base62Id"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceSetRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceSetRequest:
    out: DeleteResourceSetRequest = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("DeleteResourceSetRequest.identifier required")
    return out
