"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeBundleAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_associated_resource_type_list
    import capo_workspaces.types.bundle_id


class DescribeBundleAssociationsRequest(TypedDict, closed=True):
    bundle_id: "capo_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle.</p>"""
    associated_resource_types: "capo_workspaces.types.bundle_associated_resource_type_list.BundleAssociatedResourceTypeList"
    """<p>The resource types of the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBundleAssociationsRequest) -> dict:
    out: dict = {}
    out["BundleId"] = value["bundle_id"]
    import capo_workspaces.types.bundle_associated_resource_type_list

    out["AssociatedResourceTypes"] = (
        capo_workspaces.types.bundle_associated_resource_type_list.serialize_aws_json_1_1(
            value["associated_resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBundleAssociationsRequest:
    out: DescribeBundleAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    else:
        raise DeserializationError(
            "DescribeBundleAssociationsRequest.bundle_id required"
        )
    if "AssociatedResourceTypes" in data:
        import capo_workspaces.types.bundle_associated_resource_type_list

        out["associated_resource_types"] = (
            capo_workspaces.types.bundle_associated_resource_type_list.deserialize_aws_json_1_1(
                data["AssociatedResourceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBundleAssociationsRequest.associated_resource_types required"
        )
    return out
