"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIdNamespaceAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_namespace_association_summary_list
    import aws_sdk_cleanrooms.types.pagination_token


class ListIdNamespaceAssociationsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The token value provided to access the next page of results.</p>"""
    id_namespace_association_summaries: "aws_sdk_cleanrooms.types.id_namespace_association_summary_list.IdNamespaceAssociationSummaryList"
    """<p>The summary information of the ID namespace associations that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdNamespaceAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.id_namespace_association_summary_list

    out["idNamespaceAssociationSummaries"] = (
        aws_sdk_cleanrooms.types.id_namespace_association_summary_list.serialize_json(
            value["id_namespace_association_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListIdNamespaceAssociationsOutput:
    out: ListIdNamespaceAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "idNamespaceAssociationSummaries" in data:
        import aws_sdk_cleanrooms.types.id_namespace_association_summary_list

        out["id_namespace_association_summaries"] = (
            aws_sdk_cleanrooms.types.id_namespace_association_summary_list.deserialize_json(
                data["idNamespaceAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListIdNamespaceAssociationsOutput.id_namespace_association_summaries required"
        )
    return out
