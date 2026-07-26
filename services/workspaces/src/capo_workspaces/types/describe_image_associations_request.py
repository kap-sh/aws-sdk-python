"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeImageAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.image_associated_resource_type_list
    import capo_workspaces.types.workspace_image_id


class DescribeImageAssociationsRequest(TypedDict, closed=True):
    image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""
    associated_resource_types: "capo_workspaces.types.image_associated_resource_type_list.ImageAssociatedResourceTypeList"
    """<p>The resource types of the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageAssociationsRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    import capo_workspaces.types.image_associated_resource_type_list

    out["AssociatedResourceTypes"] = (
        capo_workspaces.types.image_associated_resource_type_list.serialize_aws_json_1_1(
            value["associated_resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageAssociationsRequest:
    out: DescribeImageAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError("DescribeImageAssociationsRequest.image_id required")
    if "AssociatedResourceTypes" in data:
        import capo_workspaces.types.image_associated_resource_type_list

        out["associated_resource_types"] = (
            capo_workspaces.types.image_associated_resource_type_list.deserialize_aws_json_1_1(
                data["AssociatedResourceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeImageAssociationsRequest.associated_resource_types required"
        )
    return out
