"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteSessionResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Returns the ID of the deleted session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSessionResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSessionResponse:
    out: DeleteSessionResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
