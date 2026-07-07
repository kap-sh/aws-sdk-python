"""Generated from Smithy shape ``com.amazonaws.elasticache#CustomerNodeEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string


class CustomerNodeEndpoint(TypedDict, closed=True):
    address: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The address of the node endpoint</p>"""
    port: NotRequired["aws_sdk_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The port of the node endpoint</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomerNodeEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "address" in value:
        pairs.append((f"{prefix}.Address", str(value["address"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))


def deserialize_query(el: Element) -> CustomerNodeEndpoint:
    out: CustomerNodeEndpoint = {}  # type: ignore[typeddict-item]
    child_address = el.find("Address")
    if child_address is not None:
        out["address"] = str(child_address.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    return out
