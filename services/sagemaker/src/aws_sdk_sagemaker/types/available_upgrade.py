"""Generated from Smithy shape ``com.amazonaws.sagemaker#AvailableUpgrade``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.major_minor_version
    import aws_sdk_sagemaker.types.release_notes_list


class AvailableUpgrade(TypedDict, closed=True):
    version: NotRequired[
        "aws_sdk_sagemaker.types.major_minor_version.MajorMinorVersion"
    ]
    """<p>The semantic version number of the available upgrade for the SageMaker Partner AI App.</p>"""
    release_notes: NotRequired[
        "aws_sdk_sagemaker.types.release_notes_list.ReleaseNotesList"
    ]
    """<p>A list of release notes describing the changes and improvements included in the available upgrade version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailableUpgrade) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "release_notes" in value:
        import aws_sdk_sagemaker.types.release_notes_list

        out["ReleaseNotes"] = (
            aws_sdk_sagemaker.types.release_notes_list.serialize_aws_json_1_1(
                value["release_notes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AvailableUpgrade:
    out: AvailableUpgrade = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "ReleaseNotes" in data:
        import aws_sdk_sagemaker.types.release_notes_list

        out["release_notes"] = (
            aws_sdk_sagemaker.types.release_notes_list.deserialize_aws_json_1_1(
                data["ReleaseNotes"]
            )
        )
    return out
