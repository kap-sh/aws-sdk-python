"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DeleteNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn


class DeleteNamespaceRequest(TypedDict, closed=True):
    id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the namespace that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteNamespaceRequest.id required")
    return out
