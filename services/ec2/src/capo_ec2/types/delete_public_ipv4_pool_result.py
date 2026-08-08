"""Generated from Smithy shape ``com.amazonaws.ec2#DeletePublicIpv4PoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class DeletePublicIpv4PoolResult(TypedDict, closed=True):
    return_value: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Information about the result of deleting the public IPv4 pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeletePublicIpv4PoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return_value" in value:
        pairs.append(
            (f"{key_prefix}ReturnValue", "true" if value["return_value"] else "false")
        )


def deserialize_ec2_query(el: Element) -> DeletePublicIpv4PoolResult:
    out: DeletePublicIpv4PoolResult = {}  # type: ignore[typeddict-item]
    child_return_value = el.find("returnValue")
    if child_return_value is not None:
        out["return_value"] = (child_return_value.text or "").lower() == "true"
    return out
