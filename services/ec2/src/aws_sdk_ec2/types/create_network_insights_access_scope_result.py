"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsAccessScopeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope
    import aws_sdk_ec2.types.network_insights_access_scope_content


class CreateNetworkInsightsAccessScopeResult(TypedDict):
    network_insights_access_scope: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope.NetworkInsightsAccessScope"
    ]
    """<p>The Network Access Scope.</p>"""
    network_insights_access_scope_content: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_content.NetworkInsightsAccessScopeContent"
    ]
    """<p>The Network Access Scope content.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInsightsAccessScopeResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope" in value:
        import aws_sdk_ec2.types.network_insights_access_scope

        aws_sdk_ec2.types.network_insights_access_scope.serialize_ec2_query(
            value["network_insights_access_scope"],
            pairs,
            f"{prefix}.NetworkInsightsAccessScope",
        )
    if "network_insights_access_scope_content" in value:
        import aws_sdk_ec2.types.network_insights_access_scope_content

        aws_sdk_ec2.types.network_insights_access_scope_content.serialize_ec2_query(
            value["network_insights_access_scope_content"],
            pairs,
            f"{prefix}.NetworkInsightsAccessScopeContent",
        )


def deserialize_ec2_query(el: Element) -> CreateNetworkInsightsAccessScopeResult:
    out: CreateNetworkInsightsAccessScopeResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope = el.find("NetworkInsightsAccessScope")
    if child_network_insights_access_scope is not None:
        import aws_sdk_ec2.types.network_insights_access_scope

        out["network_insights_access_scope"] = (
            aws_sdk_ec2.types.network_insights_access_scope.deserialize_ec2_query(
                child_network_insights_access_scope
            )
        )
    child_network_insights_access_scope_content = el.find(
        "NetworkInsightsAccessScopeContent"
    )
    if child_network_insights_access_scope_content is not None:
        import aws_sdk_ec2.types.network_insights_access_scope_content

        out["network_insights_access_scope_content"] = (
            aws_sdk_ec2.types.network_insights_access_scope_content.deserialize_ec2_query(
                child_network_insights_access_scope_content
            )
        )
    return out
