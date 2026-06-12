"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.error_message
    import aws_sdk_resiliencehub.types.string255


class ResourceError(TypedDict):
    logical_resource_id: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Identifier of the logical resource. </p>"""
    physical_resource_id: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Identifier of the physical resource. </p>"""
    reason: NotRequired["aws_sdk_resiliencehub.types.error_message.ErrorMessage"]
    """<p> This is the error message. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceError) -> dict:
    out: dict = {}
    if "logical_resource_id" in value:
        out["logicalResourceId"] = value["logical_resource_id"]
    if "physical_resource_id" in value:
        out["physicalResourceId"] = value["physical_resource_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ResourceError:
    out: ResourceError = {}  # type: ignore[typeddict-item]
    if "logicalResourceId" in data:
        out["logical_resource_id"] = data["logicalResourceId"]
    if "physicalResourceId" in data:
        out["physical_resource_id"] = data["physicalResourceId"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
