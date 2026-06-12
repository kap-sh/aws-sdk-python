"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserHierarchyStructureRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_structure_update
    import aws_sdk_connect.types.instance_id


class UpdateUserHierarchyStructureRequest(TypedDict):
    hierarchy_structure: (
        "aws_sdk_connect.types.hierarchy_structure_update.HierarchyStructureUpdate"
    )
    """<p>The hierarchy levels to update.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserHierarchyStructureRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.hierarchy_structure_update

    out["HierarchyStructure"] = (
        aws_sdk_connect.types.hierarchy_structure_update.serialize_json(
            value["hierarchy_structure"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateUserHierarchyStructureRequest:
    out: UpdateUserHierarchyStructureRequest = {}  # type: ignore[typeddict-item]
    if "HierarchyStructure" in data:
        import aws_sdk_connect.types.hierarchy_structure_update

        out["hierarchy_structure"] = (
            aws_sdk_connect.types.hierarchy_structure_update.deserialize_json(
                data["HierarchyStructure"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserHierarchyStructureRequest.hierarchy_structure required"
        )
    return out
