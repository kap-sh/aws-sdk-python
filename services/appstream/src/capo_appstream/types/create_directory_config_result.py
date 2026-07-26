"""Generated from Smithy shape ``com.amazonaws.appstream#CreateDirectoryConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.directory_config


class CreateDirectoryConfigResult(TypedDict, closed=True):
    directory_config: NotRequired[
        "capo_appstream.types.directory_config.DirectoryConfig"
    ]
    """<p>Information about the directory configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectoryConfigResult) -> dict:
    out: dict = {}
    if "directory_config" in value:
        import capo_appstream.types.directory_config

        out["DirectoryConfig"] = (
            capo_appstream.types.directory_config.serialize_aws_json_1_1(
                value["directory_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectoryConfigResult:
    out: CreateDirectoryConfigResult = {}  # type: ignore[typeddict-item]
    if "DirectoryConfig" in data:
        import capo_appstream.types.directory_config

        out["directory_config"] = (
            capo_appstream.types.directory_config.deserialize_aws_json_1_1(
                data["DirectoryConfig"]
            )
        )
    return out
