"""Generated from Smithy shape ``com.amazonaws.firehose#FailureDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_failure_type
    import aws_sdk_firehose.types.non_empty_string


class FailureDescription(TypedDict):
    type: (
        "aws_sdk_firehose.types.delivery_stream_failure_type.DeliveryStreamFailureType"
    )
    """<p>The type of error that caused the failure.</p>"""
    details: "aws_sdk_firehose.types.non_empty_string.NonEmptyString"
    """<p>A message providing details about the error that caused the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDescription) -> dict:
    out: dict = {}
    import aws_sdk_firehose.types.delivery_stream_failure_type

    out["Type"] = (
        aws_sdk_firehose.types.delivery_stream_failure_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    out["Details"] = value["details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDescription:
    out: FailureDescription = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_firehose.types.delivery_stream_failure_type

        out["type"] = (
            aws_sdk_firehose.types.delivery_stream_failure_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("FailureDescription.type required")
    if "Details" in data:
        out["details"] = data["Details"]
    else:
        raise DeserializationError("FailureDescription.details required")
    return out
