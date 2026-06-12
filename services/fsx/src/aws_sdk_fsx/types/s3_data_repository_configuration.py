"""Generated from Smithy shape ``com.amazonaws.fsx#S3DataRepositoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.auto_export_policy
    import aws_sdk_fsx.types.auto_import_policy


class S3DataRepositoryConfiguration(TypedDict):
    auto_import_policy: NotRequired[
        "aws_sdk_fsx.types.auto_import_policy.AutoImportPolicy"
    ]
    """<p>Specifies the type of updated objects (new, changed, deleted) that will be automatically imported from the linked S3 bucket to your file system.</p>"""
    auto_export_policy: NotRequired[
        "aws_sdk_fsx.types.auto_export_policy.AutoExportPolicy"
    ]
    """<p>Specifies the type of updated objects (new, changed, deleted) that will be automatically exported from your file system to the linked S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataRepositoryConfiguration) -> dict:
    out: dict = {}
    if "auto_import_policy" in value:
        import aws_sdk_fsx.types.auto_import_policy

        out["AutoImportPolicy"] = (
            aws_sdk_fsx.types.auto_import_policy.serialize_aws_json_1_1(
                value["auto_import_policy"]
            )
        )
    if "auto_export_policy" in value:
        import aws_sdk_fsx.types.auto_export_policy

        out["AutoExportPolicy"] = (
            aws_sdk_fsx.types.auto_export_policy.serialize_aws_json_1_1(
                value["auto_export_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DataRepositoryConfiguration:
    out: S3DataRepositoryConfiguration = {}  # type: ignore[typeddict-item]
    if "AutoImportPolicy" in data:
        import aws_sdk_fsx.types.auto_import_policy

        out["auto_import_policy"] = (
            aws_sdk_fsx.types.auto_import_policy.deserialize_aws_json_1_1(
                data["AutoImportPolicy"]
            )
        )
    if "AutoExportPolicy" in data:
        import aws_sdk_fsx.types.auto_export_policy

        out["auto_export_policy"] = (
            aws_sdk_fsx.types.auto_export_policy.deserialize_aws_json_1_1(
                data["AutoExportPolicy"]
            )
        )
    return out
