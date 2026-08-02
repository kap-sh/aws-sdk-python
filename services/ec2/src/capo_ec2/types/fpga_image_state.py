"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fpga_image_state_code
    import capo_ec2.types.string


class FpgaImageState(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.fpga_image_state_code.FpgaImageStateCode"]
    """<p>The state. The following are the possible values:</p> <ul> <li> <p> <code>pending</code> - AFI bitstream generation is in progress.</p> </li> <li> <p> <code>available</code> - The AFI is available for use.</p> </li> <li> <p> <code>failed</code> - AFI bitstream generation failed.</p> </li> <li> <p> <code>unavailable</code> - The AFI is no longer available for use.</p> </li> </ul>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>If the state is <code>failed</code>, this is the error message.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImageState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_ec2.types.fpga_image_state_code

        capo_ec2.types.fpga_image_state_code.serialize_ec2_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> FpgaImageState:
    out: FpgaImageState = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import capo_ec2.types.fpga_image_state_code

        out["code"] = capo_ec2.types.fpga_image_state_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
