"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DetachFromIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.object_reference


class DetachFromIndexRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the directory the index and object exist in.</p>"""
    index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the index object.</p>"""
    target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object being detached from the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachFromIndexRequest) -> dict:
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


def deserialize_json(data: dict) -> DetachFromIndexRequest:
    out: DetachFromIndexRequest = {}  # type: ignore[typeddict-item]
    if "IndexReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["index_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("DetachFromIndexRequest.index_reference required")
    if "TargetReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["target_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["TargetReference"]
            )
        )
    else:
        raise DeserializationError("DetachFromIndexRequest.target_reference required")
    return out
