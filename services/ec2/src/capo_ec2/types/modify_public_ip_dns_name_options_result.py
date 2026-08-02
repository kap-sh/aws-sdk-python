"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPublicIpDnsNameOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ModifyPublicIpDnsNameOptionsResult(TypedDict, closed=True):
    successful: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Whether or not the request was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyPublicIpDnsNameOptionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful" in value:
        pairs.append(
            (f"{key_prefix}Successful", "true" if value["successful"] else "false")
        )


def deserialize_ec2_query(el: Element) -> ModifyPublicIpDnsNameOptionsResult:
    out: ModifyPublicIpDnsNameOptionsResult = {}  # type: ignore[typeddict-item]
    child_successful = el.find("Successful")
    if child_successful is not None:
        out["successful"] = (child_successful.text or "").lower() == "true"
    return out
