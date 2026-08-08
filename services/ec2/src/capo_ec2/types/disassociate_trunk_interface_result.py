"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTrunkInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string

DisassociateTrunkInterfaceResult = TypedDict(
    "DisassociateTrunkInterfaceResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "client_token": NotRequired["capo_ec2.types.string.String"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateTrunkInterfaceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", "true" if value["return"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> DisassociateTrunkInterfaceResult:
    out: DisassociateTrunkInterfaceResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
