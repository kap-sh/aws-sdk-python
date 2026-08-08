"""Generated from Smithy shape ``com.amazonaws.ec2#EncryptionSupport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.encryption_state_value
    import capo_ec2.types.string


class EncryptionSupport(TypedDict, closed=True):
    encryption_state: NotRequired[
        "capo_ec2.types.encryption_state_value.EncryptionStateValue"
    ]
    """<p>The current encryption state of the resource.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message describing the encryption state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EncryptionSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "encryption_state" in value:
        import capo_ec2.types.encryption_state_value

        capo_ec2.types.encryption_state_value.serialize_ec2_query(
            value["encryption_state"], pairs, f"{key_prefix}EncryptionState"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))


def deserialize_ec2_query(el: Element) -> EncryptionSupport:
    out: EncryptionSupport = {}  # type: ignore[typeddict-item]
    child_encryption_state = el.find("encryptionState")
    if child_encryption_state is not None:
        import capo_ec2.types.encryption_state_value

        out["encryption_state"] = (
            capo_ec2.types.encryption_state_value.deserialize_ec2_query(
                child_encryption_state
            )
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    return out
