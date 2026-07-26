"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetMembershipDatasourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.membership_datasources_list
    import capo_detective.types.unprocessed_graph_list


class BatchGetMembershipDatasourcesResponse(TypedDict, closed=True):
    membership_datasources: NotRequired[
        "capo_detective.types.membership_datasources_list.MembershipDatasourcesList"
    ]
    """<p>Details on the data source package history for an member of the behavior graph.</p>"""
    unprocessed_graphs: NotRequired[
        "capo_detective.types.unprocessed_graph_list.UnprocessedGraphList"
    ]
    """<p>Graphs that data source package information could not be retrieved for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMembershipDatasourcesResponse) -> dict:
    out: dict = {}
    if "membership_datasources" in value:
        import capo_detective.types.membership_datasources_list

        out["MembershipDatasources"] = (
            capo_detective.types.membership_datasources_list.serialize_json(
                value["membership_datasources"]
            )
        )
    if "unprocessed_graphs" in value:
        import capo_detective.types.unprocessed_graph_list

        out["UnprocessedGraphs"] = (
            capo_detective.types.unprocessed_graph_list.serialize_json(
                value["unprocessed_graphs"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetMembershipDatasourcesResponse:
    out: BatchGetMembershipDatasourcesResponse = {}  # type: ignore[typeddict-item]
    if "MembershipDatasources" in data:
        import capo_detective.types.membership_datasources_list

        out["membership_datasources"] = (
            capo_detective.types.membership_datasources_list.deserialize_json(
                data["MembershipDatasources"]
            )
        )
    if "UnprocessedGraphs" in data:
        import capo_detective.types.unprocessed_graph_list

        out["unprocessed_graphs"] = (
            capo_detective.types.unprocessed_graph_list.deserialize_json(
                data["UnprocessedGraphs"]
            )
        )
    return out
