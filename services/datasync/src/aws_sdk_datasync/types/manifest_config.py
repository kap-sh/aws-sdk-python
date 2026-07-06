"""Generated from Smithy shape ``com.amazonaws.datasync#ManifestConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.manifest_action
    import aws_sdk_datasync.types.manifest_format
    import aws_sdk_datasync.types.source_manifest_config


class ManifestConfig(TypedDict, closed=True):
    action: NotRequired["aws_sdk_datasync.types.manifest_action.ManifestAction"]
    """<p>Specifies what DataSync uses the manifest for.</p>"""
    format: NotRequired["aws_sdk_datasync.types.manifest_format.ManifestFormat"]
    r"""<p>Specifies the file format of your manifest. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-create\">Creating a manifest</a>.</p>"""
    source: NotRequired[
        "aws_sdk_datasync.types.source_manifest_config.SourceManifestConfig"
    ]
    r"""<p>Specifies the manifest that you want DataSync to use and where it's hosted.</p> <note> <p>You must specify this parameter if you're configuring a new manifest on or after February 7, 2024.</p> <p>If you don't, you'll get a 400 status code and <code>ValidationException</code> error stating that you're missing the IAM role for DataSync to access the S3 bucket where you're hosting your manifest. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access\">Providing DataSync access to your manifest</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManifestConfig) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_datasync.types.manifest_action

        out["Action"] = aws_sdk_datasync.types.manifest_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "format" in value:
        import aws_sdk_datasync.types.manifest_format

        out["Format"] = aws_sdk_datasync.types.manifest_format.serialize_aws_json_1_1(
            value["format"]
        )
    if "source" in value:
        import aws_sdk_datasync.types.source_manifest_config

        out["Source"] = (
            aws_sdk_datasync.types.source_manifest_config.serialize_aws_json_1_1(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManifestConfig:
    out: ManifestConfig = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_datasync.types.manifest_action

        out["action"] = aws_sdk_datasync.types.manifest_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "Format" in data:
        import aws_sdk_datasync.types.manifest_format

        out["format"] = aws_sdk_datasync.types.manifest_format.deserialize_aws_json_1_1(
            data["Format"]
        )
    if "Source" in data:
        import aws_sdk_datasync.types.source_manifest_config

        out["source"] = (
            aws_sdk_datasync.types.source_manifest_config.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    return out
