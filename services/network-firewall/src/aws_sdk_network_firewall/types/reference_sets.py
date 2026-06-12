"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ReferenceSets``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.ip_set_reference_map


class ReferenceSets(TypedDict):
    ip_set_references: NotRequired[
        "aws_sdk_network_firewall.types.ip_set_reference_map.IPSetReferenceMap"
    ]
    """<p>The list of IP set references.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReferenceSets) -> dict:
    out: dict = {}
    if "ip_set_references" in value:
        import aws_sdk_network_firewall.types.ip_set_reference_map

        out["IPSetReferences"] = (
            aws_sdk_network_firewall.types.ip_set_reference_map.serialize_aws_json_1_0(
                value["ip_set_references"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReferenceSets:
    out: ReferenceSets = {}  # type: ignore[typeddict-item]
    if "IPSetReferences" in data:
        import aws_sdk_network_firewall.types.ip_set_reference_map

        out["ip_set_references"] = (
            aws_sdk_network_firewall.types.ip_set_reference_map.deserialize_aws_json_1_0(
                data["IPSetReferences"]
            )
        )
    return out
