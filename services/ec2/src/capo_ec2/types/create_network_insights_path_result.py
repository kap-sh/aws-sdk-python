"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsPathResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_insights_path


class CreateNetworkInsightsPathResult(TypedDict, closed=True):
    network_insights_path: NotRequired[
        "capo_ec2.types.network_insights_path.NetworkInsightsPath"
    ]
    """<p>Information about the path.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInsightsPathResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_insights_path" in value:
        import capo_ec2.types.network_insights_path

        capo_ec2.types.network_insights_path.serialize_ec2_query(
            value["network_insights_path"], pairs, f"{key_prefix}NetworkInsightsPath"
        )


def deserialize_ec2_query(el: Element) -> CreateNetworkInsightsPathResult:
    out: CreateNetworkInsightsPathResult = {}  # type: ignore[typeddict-item]
    child_network_insights_path = el.find("NetworkInsightsPath")
    if child_network_insights_path is not None:
        import capo_ec2.types.network_insights_path

        out["network_insights_path"] = (
            capo_ec2.types.network_insights_path.deserialize_ec2_query(
                child_network_insights_path
            )
        )
    return out
