"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteKeyPairResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string

DeleteKeyPairResult = TypedDict(
    "DeleteKeyPairResult",
    {
        "return": NotRequired["capo_ec2.types.boolean.Boolean"],
        "key_pair_id": NotRequired["capo_ec2.types.string.String"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteKeyPairResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", "true" if value["return"] else "false"))
    if "key_pair_id" in value:
        pairs.append((f"{key_prefix}KeyPairId", str(value["key_pair_id"])))


def deserialize_ec2_query(el: Element) -> DeleteKeyPairResult:
    out: DeleteKeyPairResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_key_pair_id = el.find("KeyPairId")
    if child_key_pair_id is not None:
        out["key_pair_id"] = str(child_key_pair_id.text or "")
    return out
