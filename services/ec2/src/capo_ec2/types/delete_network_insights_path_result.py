"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsPathResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_path_id


class DeleteNetworkInsightsPathResult(TypedDict, closed=True):
    network_insights_path_id: NotRequired[
        "capo_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsPathResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_path_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInsightsPathId",
                str(value["network_insights_path_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteNetworkInsightsPathResult:
    out: DeleteNetworkInsightsPathResult = {}  # type: ignore[typeddict-item]
    child_network_insights_path_id = el.find("networkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    return out
