"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.resource_list


class ListResourcesOutput(TypedDict):
    resources: NotRequired[
        "aws_sdk_resource_explorer_2.types.resource_list.ResourceList"
    ]
    """<p>The list of structures that describe the resources that match the query. </p>"""
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""
    view_arn: NotRequired["str"]
    """<p>The Amazon resource name (ARN) of the view that this operation used to perform the search. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesOutput) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_resource_explorer_2.types.resource_list

        out["Resources"] = (
            aws_sdk_resource_explorer_2.types.resource_list.serialize_json(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    return out


def deserialize_json(data: dict) -> ListResourcesOutput:
    out: ListResourcesOutput = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_resource_explorer_2.types.resource_list

        out["resources"] = (
            aws_sdk_resource_explorer_2.types.resource_list.deserialize_json(
                data["Resources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ViewArn" in data:
        out["view_arn"] = data["ViewArn"]
    return out
