"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdNamespacesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_namespace_list
    import aws_sdk_entityresolution.types.next_token


class ListIdNamespacesOutput(TypedDict):
    id_namespace_summaries: NotRequired[
        "aws_sdk_entityresolution.types.id_namespace_list.IdNamespaceList"
    ]
    """<p>A list of <code>IdNamespaceSummaries</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdNamespacesOutput) -> dict:
    out: dict = {}
    if "id_namespace_summaries" in value:
        import aws_sdk_entityresolution.types.id_namespace_list

        out["idNamespaceSummaries"] = (
            aws_sdk_entityresolution.types.id_namespace_list.serialize_json(
                value["id_namespace_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdNamespacesOutput:
    out: ListIdNamespacesOutput = {}  # type: ignore[typeddict-item]
    if "idNamespaceSummaries" in data:
        import aws_sdk_entityresolution.types.id_namespace_list

        out["id_namespace_summaries"] = (
            aws_sdk_entityresolution.types.id_namespace_list.deserialize_json(
                data["idNamespaceSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
