"""Generated from Smithy shape ``com.amazonaws.codecommit#FileModes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_mode_type_enum


class FileModes(TypedDict, closed=True):
    source: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode of a file in the source of a merge or pull request.</p>"""
    destination: NotRequired[
        "capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The file mode of a file in the destination of a merge or pull request.</p>"""
    base: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode of a file in the base of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileModes) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["source"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "destination" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["destination"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "base" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["base"] = capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
            value["base"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileModes:
    out: FileModes = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["source"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    if "destination" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["destination"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if "base" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["base"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["base"]
            )
        )
    return out
