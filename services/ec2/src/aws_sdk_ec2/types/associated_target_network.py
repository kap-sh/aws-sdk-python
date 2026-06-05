"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedTargetNetwork``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_network_type
    import aws_sdk_ec2.types.string


class AssociatedTargetNetwork(TypedDict):
    network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    network_type: NotRequired[
        "aws_sdk_ec2.types.associated_network_type.AssociatedNetworkType"
    ]
    """<p>The target network type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedTargetNetwork, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_id" in value:
        pairs.append((f"{prefix}.NetworkId", str(value["network_id"])))
    if "network_type" in value:
        import aws_sdk_ec2.types.associated_network_type

        aws_sdk_ec2.types.associated_network_type.serialize_ec2_query(
            value["network_type"], pairs, f"{prefix}.NetworkType"
        )


def deserialize_ec2_query(el: Element) -> AssociatedTargetNetwork:
    out: AssociatedTargetNetwork = {}  # type: ignore[typeddict-item]
    child_network_id = el.find("NetworkId")
    if child_network_id is not None:
        out["network_id"] = str(child_network_id.text or "")
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        import aws_sdk_ec2.types.associated_network_type

        out["network_type"] = (
            aws_sdk_ec2.types.associated_network_type.deserialize_ec2_query(
                child_network_type
            )
        )
    return out
