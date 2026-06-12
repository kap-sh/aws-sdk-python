"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateAccessPointOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.dns_name


class CreateAccessPointOutput(TypedDict):
    dns_name: NotRequired["aws_sdk_elastic_load_balancing.types.dns_name.DNSName"]
    """<p>The DNS name of the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAccessPointOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dns_name" in value:
        pairs.append((f"{prefix}.DNSName", str(value["dns_name"])))


def deserialize_query(el: Element) -> CreateAccessPointOutput:
    out: CreateAccessPointOutput = {}  # type: ignore[typeddict-item]
    child_dns_name = el.find("DNSName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    return out
