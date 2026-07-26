"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_in_list

ClusterList: TypeAlias = list["capo_docdb_elastic.types.cluster_in_list.ClusterInList"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterList) -> list:
    import capo_docdb_elastic.types.cluster_in_list

    out: list = []
    for item in value:
        out.append(capo_docdb_elastic.types.cluster_in_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterList:
    import capo_docdb_elastic.types.cluster_in_list

    out: ClusterList = []
    for item in data:
        out.append(capo_docdb_elastic.types.cluster_in_list.deserialize_json(item))
    return out
