"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsAccessScopeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_id


class DeleteNetworkInsightsAccessScopeResult(TypedDict):
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsAccessScopeResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_insights_access_scope_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsAccessScopeId",
                str(value["network_insights_access_scope_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteNetworkInsightsAccessScopeResult:
    out: DeleteNetworkInsightsAccessScopeResult = {}  # type: ignore[typeddict-item]
    child_network_insights_access_scope_id = el.find("NetworkInsightsAccessScopeId")
    if child_network_insights_access_scope_id is not None:
        out["network_insights_access_scope_id"] = str(
            child_network_insights_access_scope_id.text or ""
        )
    return out
