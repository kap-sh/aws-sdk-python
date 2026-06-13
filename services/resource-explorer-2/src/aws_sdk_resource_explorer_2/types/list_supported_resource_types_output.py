"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListSupportedResourceTypesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.resource_type_list


class ListSupportedResourceTypesOutput(TypedDict):
    resource_types: NotRequired[
        "aws_sdk_resource_explorer_2.types.resource_type_list.ResourceTypeList"
    ]
    """<p>The list of resource types supported by Resource Explorer.</p>"""
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportedResourceTypesOutput) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import aws_sdk_resource_explorer_2.types.resource_type_list

        out["ResourceTypes"] = (
            aws_sdk_resource_explorer_2.types.resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupportedResourceTypesOutput:
    out: ListSupportedResourceTypesOutput = {}  # type: ignore[typeddict-item]
    if "ResourceTypes" in data:
        import aws_sdk_resource_explorer_2.types.resource_type_list

        out["resource_types"] = (
            aws_sdk_resource_explorer_2.types.resource_type_list.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
