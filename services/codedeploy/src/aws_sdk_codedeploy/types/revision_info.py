"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.generic_revision_info
    import aws_sdk_codedeploy.types.revision_location


class RevisionInfo(TypedDict):
    revision_location: NotRequired[
        "aws_sdk_codedeploy.types.revision_location.RevisionLocation"
    ]
    """<p>Information about the location and type of an application revision.</p>"""
    generic_revision_info: NotRequired[
        "aws_sdk_codedeploy.types.generic_revision_info.GenericRevisionInfo"
    ]
    """<p>Information about an application revision, including usage details and associated deployment groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionInfo) -> dict:
    out: dict = {}
    if "revision_location" in value:
        import aws_sdk_codedeploy.types.revision_location

        out["revisionLocation"] = (
            aws_sdk_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision_location"]
            )
        )
    if "generic_revision_info" in value:
        import aws_sdk_codedeploy.types.generic_revision_info

        out["genericRevisionInfo"] = (
            aws_sdk_codedeploy.types.generic_revision_info.serialize_aws_json_1_1(
                value["generic_revision_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevisionInfo:
    out: RevisionInfo = {}  # type: ignore[typeddict-item]
    if "revisionLocation" in data:
        import aws_sdk_codedeploy.types.revision_location

        out["revision_location"] = (
            aws_sdk_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revisionLocation"]
            )
        )
    if "genericRevisionInfo" in data:
        import aws_sdk_codedeploy.types.generic_revision_info

        out["generic_revision_info"] = (
            aws_sdk_codedeploy.types.generic_revision_info.deserialize_aws_json_1_1(
                data["genericRevisionInfo"]
            )
        )
    return out
