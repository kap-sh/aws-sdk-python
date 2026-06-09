"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageDeregistrationProtectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

DisableImageDeregistrationProtectionResult = TypedDict(
    "DisableImageDeregistrationProtectionResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.string.String"],
    },
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableImageDeregistrationProtectionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", str(value["return"])))


def deserialize_ec2_query(el: Element) -> DisableImageDeregistrationProtectionResult:
    out: DisableImageDeregistrationProtectionResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = str(child_return.text or "")
    return out
