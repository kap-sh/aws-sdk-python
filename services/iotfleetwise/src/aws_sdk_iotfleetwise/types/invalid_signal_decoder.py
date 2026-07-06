"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignalDecoder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fully_qualified_name
    import aws_sdk_iotfleetwise.types.message
    import aws_sdk_iotfleetwise.types.signal_decoder_failure_reason


class InvalidSignalDecoder(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_iotfleetwise.types.fully_qualified_name.FullyQualifiedName"
    ]
    """<p>The name of a signal decoder that isn't valid.</p>"""
    reason: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_decoder_failure_reason.SignalDecoderFailureReason"
    ]
    """<p>A message about why the signal decoder isn't valid.</p>"""
    hint: NotRequired["aws_sdk_iotfleetwise.types.message.message"]
    """<p>The possible cause for the invalid signal decoder.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSignalDecoder) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "reason" in value:
        import aws_sdk_iotfleetwise.types.signal_decoder_failure_reason

        out["reason"] = (
            aws_sdk_iotfleetwise.types.signal_decoder_failure_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    if "hint" in value:
        out["hint"] = value["hint"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidSignalDecoder:
    out: InvalidSignalDecoder = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "reason" in data:
        import aws_sdk_iotfleetwise.types.signal_decoder_failure_reason

        out["reason"] = (
            aws_sdk_iotfleetwise.types.signal_decoder_failure_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    if "hint" in data:
        out["hint"] = data["hint"]
    return out
