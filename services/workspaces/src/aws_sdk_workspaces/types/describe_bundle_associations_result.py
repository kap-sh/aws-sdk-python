"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeBundleAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_resource_association_list


class DescribeBundleAssociationsResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_workspaces.types.bundle_resource_association_list.BundleResourceAssociationList"
    ]
    """<p>List of information about the specified associations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBundleAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_workspaces.types.bundle_resource_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.bundle_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBundleAssociationsResult:
    out: DescribeBundleAssociationsResult = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_workspaces.types.bundle_resource_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.bundle_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
