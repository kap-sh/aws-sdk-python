"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsListValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Phase2EncryptionAlgorithmsListValue(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The encryption algorithm.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2EncryptionAlgorithmsListValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> Phase2EncryptionAlgorithmsListValue:
    out: Phase2EncryptionAlgorithmsListValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
