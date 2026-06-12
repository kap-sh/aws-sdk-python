"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#RawMessageContent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmailmessageflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.s3_reference


class RawMessageContent(TypedDict):
    s3_reference: "aws_sdk_workmailmessageflow.types.s3_reference.S3Reference"
    """<p>The S3 reference of an email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RawMessageContent) -> dict:
    out: dict = {}
    import aws_sdk_workmailmessageflow.types.s3_reference

    out["s3Reference"] = aws_sdk_workmailmessageflow.types.s3_reference.serialize_json(
        value["s3_reference"]
    )
    return out


def deserialize_json(data: dict) -> RawMessageContent:
    out: RawMessageContent = {}  # type: ignore[typeddict-item]
    if "s3Reference" in data:
        import aws_sdk_workmailmessageflow.types.s3_reference

        out["s3_reference"] = (
            aws_sdk_workmailmessageflow.types.s3_reference.deserialize_json(
                data["s3Reference"]
            )
        )
    else:
        raise DeserializationError("RawMessageContent.s3_reference required")
    return out
