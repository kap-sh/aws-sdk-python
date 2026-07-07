"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeleteSystemInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn


class DeleteSystemInstanceRequest(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the system instance to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSystemInstanceRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSystemInstanceRequest:
    out: DeleteSystemInstanceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
