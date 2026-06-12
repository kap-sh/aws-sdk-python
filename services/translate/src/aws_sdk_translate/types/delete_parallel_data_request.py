"""Generated from Smithy shape ``com.amazonaws.translate#DeleteParallelDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.resource_name


class DeleteParallelDataRequest(TypedDict):
    name: "aws_sdk_translate.types.resource_name.ResourceName"
    """<p>The name of the parallel data resource that is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParallelDataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParallelDataRequest:
    out: DeleteParallelDataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteParallelDataRequest.name required")
    return out
