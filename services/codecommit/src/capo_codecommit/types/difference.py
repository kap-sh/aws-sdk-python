"""Generated from Smithy shape ``com.amazonaws.codecommit#Difference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.blob_metadata
    import capo_codecommit.types.change_type_enum


class Difference(TypedDict, closed=True):
    before_blob: NotRequired["capo_codecommit.types.blob_metadata.BlobMetadata"]
    """<p>Information about a <code>beforeBlob</code> data type object, including the ID, the file mode permission code, and the path.</p>"""
    after_blob: NotRequired["capo_codecommit.types.blob_metadata.BlobMetadata"]
    """<p>Information about an <code>afterBlob</code> data type object, including the ID, the file mode permission code, and the path.</p>"""
    change_type: NotRequired["capo_codecommit.types.change_type_enum.ChangeTypeEnum"]
    """<p>Whether the change type of the difference is an addition (A), deletion (D), or modification (M).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Difference) -> dict:
    out: dict = {}
    if "before_blob" in value:
        import capo_codecommit.types.blob_metadata

        out["beforeBlob"] = capo_codecommit.types.blob_metadata.serialize_aws_json_1_1(
            value["before_blob"]
        )
    if "after_blob" in value:
        import capo_codecommit.types.blob_metadata

        out["afterBlob"] = capo_codecommit.types.blob_metadata.serialize_aws_json_1_1(
            value["after_blob"]
        )
    if "change_type" in value:
        import capo_codecommit.types.change_type_enum

        out["changeType"] = (
            capo_codecommit.types.change_type_enum.serialize_aws_json_1_1(
                value["change_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Difference:
    out: Difference = {}  # type: ignore[typeddict-item]
    if "beforeBlob" in data:
        import capo_codecommit.types.blob_metadata

        out["before_blob"] = (
            capo_codecommit.types.blob_metadata.deserialize_aws_json_1_1(
                data["beforeBlob"]
            )
        )
    if "afterBlob" in data:
        import capo_codecommit.types.blob_metadata

        out["after_blob"] = (
            capo_codecommit.types.blob_metadata.deserialize_aws_json_1_1(
                data["afterBlob"]
            )
        )
    if "changeType" in data:
        import capo_codecommit.types.change_type_enum

        out["change_type"] = (
            capo_codecommit.types.change_type_enum.deserialize_aws_json_1_1(
                data["changeType"]
            )
        )
    return out
