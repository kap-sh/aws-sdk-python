"""Generated from Smithy shape ``com.amazonaws.codecommit#FileModes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_mode_type_enum


class FileModes(TypedDict):
    source: NotRequired["aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode of a file in the source of a merge or pull request.</p>"""
    destination: NotRequired[
        "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The file mode of a file in the destination of a merge or pull request.</p>"""
    base: NotRequired["aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode of a file in the base of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileModes) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "destination" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "base" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["base"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["base"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileModes:
    out: FileModes = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    if "destination" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if "base" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["base"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["base"]
            )
        )
    return out
