"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeContentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_access_scope_content


class GetNetworkInsightsAccessScopeContentResult(TypedDict, closed=True):
    network_insights_access_scope_content: NotRequired[
        "capo_ec2.types.network_insights_access_scope_content.NetworkInsightsAccessScopeContent"
    ]
    """<p>The Network Access Scope content.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetNetworkInsightsAccessScopeContentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_access_scope_content" in value:
        import capo_ec2.types.network_insights_access_scope_content

        capo_ec2.types.network_insights_access_scope_content.serialize_ec2_query(
            value["network_insights_access_scope_content"],
            pairs,
            f"{key_prefix}NetworkInsightsAccessScopeContent",
        )


def deserialize_ec2_query(el: Element) -> GetNetworkInsightsAccessScopeContentResult:
    out: GetNetworkInsightsAccessScopeContentResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_content = el.find(
        "NetworkInsightsAccessScopeContent"
    )
    if child_network_insights_access_scope_content is not None:
        import capo_ec2.types.network_insights_access_scope_content

        out["network_insights_access_scope_content"] = (
            capo_ec2.types.network_insights_access_scope_content.deserialize_ec2_query(
                child_network_insights_access_scope_content
            )
        )
    return out
