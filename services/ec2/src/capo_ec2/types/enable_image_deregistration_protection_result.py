"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageDeregistrationProtectionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string

EnableImageDeregistrationProtectionResult = TypedDict(
    "EnableImageDeregistrationProtectionResult",
    {
        "return": NotRequired["capo_ec2.types.string.String"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableImageDeregistrationProtectionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "return" in value:
        pairs.append((f"{key_prefix}Return", str(value["return"])))


def deserialize_ec2_query(el: Element) -> EnableImageDeregistrationProtectionResult:
    out: EnableImageDeregistrationProtectionResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("return")
    if child_return is not None:
        out["return"] = str(child_return.text or "")
    return out
