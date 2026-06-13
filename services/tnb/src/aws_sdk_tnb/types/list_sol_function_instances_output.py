"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstancesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_function_instance_resources
    import aws_sdk_tnb.types.pagination_token


class ListSolFunctionInstancesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    function_instances: NotRequired[
        "aws_sdk_tnb.types.list_sol_function_instance_resources.ListSolFunctionInstanceResources"
    ]
    """<p>Network function instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstancesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "function_instances" in value:
        import aws_sdk_tnb.types.list_sol_function_instance_resources

        out["functionInstances"] = (
            aws_sdk_tnb.types.list_sol_function_instance_resources.serialize_json(
                value["function_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolFunctionInstancesOutput:
    out: ListSolFunctionInstancesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "functionInstances" in data:
        import aws_sdk_tnb.types.list_sol_function_instance_resources

        out["function_instances"] = (
            aws_sdk_tnb.types.list_sol_function_instance_resources.deserialize_json(
                data["functionInstances"]
            )
        )
    return out
