"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_path_list
    import capo_ec2.types.network_insights_access_scope_id


class NetworkInsightsAccessScopeContent(TypedDict, closed=True):
    network_insights_access_scope_id: NotRequired[
        "capo_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    match_paths: NotRequired[
        "capo_ec2.types.access_scope_path_list.AccessScopePathList"
    ]
    """<p>The paths to match.</p>"""
    exclude_paths: NotRequired[
        "capo_ec2.types.access_scope_path_list.AccessScopePathList"
    ]
    """<p>The paths to exclude.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsAccessScopeContent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )
    if "match_paths" in value:
        import capo_ec2.types.access_scope_path_list

        capo_ec2.types.access_scope_path_list.serialize_ec2_query(
            value["match_paths"], pairs, f"{key_prefix}MatchPathSet"
        )
    if "exclude_paths" in value:
        import capo_ec2.types.access_scope_path_list

        capo_ec2.types.access_scope_path_list.serialize_ec2_query(
            value["exclude_paths"], pairs, f"{key_prefix}ExcludePathSet"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsAccessScopeContent:
    out: NetworkInsightsAccessScopeContent = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_id = el.find("networkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    if el.find("matchPathSet") is not None:
        import capo_ec2.types.access_scope_path_list

        out["match_paths"] = (
            capo_ec2.types.access_scope_path_list.deserialize_ec2_query(
                el, "matchPathSet"
            )
        )
    if el.find("excludePathSet") is not None:
        import capo_ec2.types.access_scope_path_list

        out["exclude_paths"] = (
            capo_ec2.types.access_scope_path_list.deserialize_ec2_query(
                el, "excludePathSet"
            )
        )
    return out
