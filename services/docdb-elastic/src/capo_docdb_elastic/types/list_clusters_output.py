"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListClustersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_list
    import capo_docdb_elastic.types.pagination_token


class ListClustersOutput(TypedDict, closed=True):
    clusters: NotRequired["capo_docdb_elastic.types.cluster_list.ClusterList"]
    """<p>A list of Amazon DocumentDB elastic clusters.</p>"""
    next_token: NotRequired["capo_docdb_elastic.types.pagination_token.PaginationToken"]
    """<p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersOutput) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_docdb_elastic.types.cluster_list

        out["clusters"] = capo_docdb_elastic.types.cluster_list.serialize_json(
            value["clusters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersOutput:
    out: ListClustersOutput = {}  # type: ignore[typeddict-item]
    if "clusters" in data:
        import capo_docdb_elastic.types.cluster_list

        out["clusters"] = capo_docdb_elastic.types.cluster_list.deserialize_json(
            data["clusters"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
