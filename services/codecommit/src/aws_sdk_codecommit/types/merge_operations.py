"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeOperations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.change_type_enum


class MergeOperations(TypedDict):
    source: NotRequired["aws_sdk_codecommit.types.change_type_enum.ChangeTypeEnum"]
    """<p>The operation (add, modify, or delete) on a file in the source of a merge or pull request.</p>"""
    destination: NotRequired["aws_sdk_codecommit.types.change_type_enum.ChangeTypeEnum"]
    """<p>The operation on a file in the destination of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeOperations) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_codecommit.types.change_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.change_type_enum.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "destination" in value:
        import aws_sdk_codecommit.types.change_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.change_type_enum.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeOperations:
    out: MergeOperations = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_codecommit.types.change_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.change_type_enum.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    if "destination" in data:
        import aws_sdk_codecommit.types.change_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.change_type_enum.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    return out
