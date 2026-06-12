"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetObjectInformationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.consistency_level
    import aws_sdk_clouddirectory.types.object_reference


class GetObjectInformationRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory being retrieved.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object.</p>"""
    consistency_level: NotRequired[
        "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>The consistency level at which to retrieve the object information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectInformationRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetObjectInformationRequest:
    out: GetObjectInformationRequest = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectInformationRequest.object_reference required"
        )
    return out
