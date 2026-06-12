"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.logical_resource_id
    import aws_sdk_resiliencehub.types.string255


class ResourceIdentifier(TypedDict):
    logical_resource_id: NotRequired[
        "aws_sdk_resiliencehub.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>Logical identifier of the drifted resource.</p>"""
    resource_type: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Type of the drifted resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdentifier) -> dict:
    out: dict = {}
    if "logical_resource_id" in value:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logicalResourceId"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.serialize_json(
                value["logical_resource_id"]
            )
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceIdentifier:
    out: ResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "logicalResourceId" in data:
        import aws_sdk_resiliencehub.types.logical_resource_id

        out["logical_resource_id"] = (
            aws_sdk_resiliencehub.types.logical_resource_id.deserialize_json(
                data["logicalResourceId"]
            )
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
