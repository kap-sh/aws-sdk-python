"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachToIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.object_reference


class AttachToIndexRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory where the object and index exist.</p>"""
    index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the index that you are attaching the object to.</p>"""
    target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object that you are attaching to the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachToIndexRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["IndexReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["index_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["TargetReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["target_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttachToIndexRequest:
    out: AttachToIndexRequest = {}  # type: ignore[typeddict-item]
    if "IndexReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["index_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("AttachToIndexRequest.index_reference required")
    if "TargetReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError("AttachToIndexRequest.target_reference required")
    return out
