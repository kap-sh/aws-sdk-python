"""Generated from Smithy shape ``com.amazonaws.grafana#ListVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.grafana_version_list
    import capo_grafana.types.pagination_token


class ListVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use in a subsequent <code>ListVersions</code> operation to return the next set of results.</p>"""
    grafana_versions: NotRequired[
        "capo_grafana.types.grafana_version_list.GrafanaVersionList"
    ]
    """<p>The Grafana versions available to create. If a workspace ID is included in the request, the Grafana versions to which this workspace can be upgraded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "grafana_versions" in value:
        import capo_grafana.types.grafana_version_list

        out["grafanaVersions"] = capo_grafana.types.grafana_version_list.serialize_json(
            value["grafana_versions"]
        )
    return out


def deserialize_json(data: dict) -> ListVersionsResponse:
    out: ListVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "grafanaVersions" in data:
        import capo_grafana.types.grafana_version_list

        out["grafana_versions"] = (
            capo_grafana.types.grafana_version_list.deserialize_json(
                data["grafanaVersions"]
            )
        )
    return out
