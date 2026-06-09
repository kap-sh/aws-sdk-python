"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageDeregistrationProtectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

EnableImageDeregistrationProtectionResult = TypedDict(
    "EnableImageDeregistrationProtectionResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.string.String"],
    },
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableImageDeregistrationProtectionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", str(value["return"])))


def deserialize_ec2_query(el: Element) -> EnableImageDeregistrationProtectionResult:
    out: EnableImageDeregistrationProtectionResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = str(child_return.text or "")
    return out
