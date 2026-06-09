"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_state_code
    import aws_sdk_ec2.types.string


class FpgaImageState(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.fpga_image_state_code.FpgaImageStateCode"]
    """<p>The state. The following are the possible values:</p> <ul> <li> <p> <code>pending</code> - AFI bitstream generation is in progress.</p> </li> <li> <p> <code>available</code> - The AFI is available for use.</p> </li> <li> <p> <code>failed</code> - AFI bitstream generation failed.</p> </li> <li> <p> <code>unavailable</code> - The AFI is no longer available for use.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the state is <code>failed</code>, this is the error message.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImageState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.fpga_image_state_code

        aws_sdk_ec2.types.fpga_image_state_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> FpgaImageState:
    out: FpgaImageState = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.fpga_image_state_code

        out["code"] = aws_sdk_ec2.types.fpga_image_state_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
