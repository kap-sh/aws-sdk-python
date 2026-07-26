"""Generated from Smithy shape ``com.amazonaws.ec2#ConfirmProductInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string

ConfirmProductInstanceResult = TypedDict(
    "ConfirmProductInstanceResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "owner_id": NotRequired["capo_ec2.types.string.String"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConfirmProductInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))


def deserialize_ec2_query(el: Element) -> ConfirmProductInstanceResult:
    out: ConfirmProductInstanceResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    return out
