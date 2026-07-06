"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreVolumeFromRecycleBinResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

RestoreVolumeFromRecycleBinResult = TypedDict(
    "RestoreVolumeFromRecycleBinResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreVolumeFromRecycleBinResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))


def deserialize_ec2_query(el: Element) -> RestoreVolumeFromRecycleBinResult:
    out: RestoreVolumeFromRecycleBinResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    return out
