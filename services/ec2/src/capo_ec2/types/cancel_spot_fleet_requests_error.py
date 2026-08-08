"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancel_batch_error_code
    import capo_ec2.types.string


class CancelSpotFleetRequestsError(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.cancel_batch_error_code.CancelBatchErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the error code.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_ec2.types.cancel_batch_error_code

        capo_ec2.types.cancel_batch_error_code.serialize_ec2_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsError:
    out: CancelSpotFleetRequestsError = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        import capo_ec2.types.cancel_batch_error_code

        out["code"] = capo_ec2.types.cancel_batch_error_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
