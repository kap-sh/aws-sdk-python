"""Generated from Smithy shape ``com.amazonaws.workmail#CreateResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.resource_id


class CreateResourceResponse(TypedDict):
    resource_id: NotRequired["aws_sdk_workmail.types.resource_id.ResourceId"]
    """<p>The identifier of the new resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceResponse) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceResponse:
    out: CreateResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out
