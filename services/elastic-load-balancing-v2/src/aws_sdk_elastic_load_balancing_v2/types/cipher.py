"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Cipher``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.cipher_name
    import aws_sdk_elastic_load_balancing_v2.types.cipher_priority


class Cipher(TypedDict):
    name: NotRequired["aws_sdk_elastic_load_balancing_v2.types.cipher_name.CipherName"]
    """<p>The name of the cipher.</p>"""
    priority: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.cipher_priority.CipherPriority"
    ]
    """<p>The priority of the cipher.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Cipher, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))


def deserialize_query(el: Element) -> Cipher:
    out: Cipher = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
