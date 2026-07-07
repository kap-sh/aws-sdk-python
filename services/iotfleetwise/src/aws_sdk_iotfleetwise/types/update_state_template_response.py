"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateStateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.resource_unique_id


class UpdateStateTemplateResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iotfleetwise.types.resource_name.resourceName"]
    """<p>The name of the state template.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the state template.</p>"""
    id: NotRequired["aws_sdk_iotfleetwise.types.resource_unique_id.ResourceUniqueId"]
    """<p>The unique ID of the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateTemplateResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateTemplateResponse:
    out: UpdateStateTemplateResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
