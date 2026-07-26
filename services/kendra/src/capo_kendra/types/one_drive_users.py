"""Generated from Smithy shape ``com.amazonaws.kendra#OneDriveUsers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.one_drive_user_list
    import capo_kendra.types.s3_path


class OneDriveUsers(TypedDict, closed=True):
    one_drive_user_list: NotRequired[
        "capo_kendra.types.one_drive_user_list.OneDriveUserList"
    ]
    """<p>A list of users whose documents should be indexed. Specify the user names in email format, for example, <code>username@tenantdomain</code>. If you need to index the documents of more than 10 users, use the <code>OneDriveUserS3Path</code> field to specify the location of a file containing a list of users.</p>"""
    one_drive_user_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    """<p>The S3 bucket location of a file containing a list of users whose documents should be indexed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OneDriveUsers) -> dict:
    out: dict = {}
    if "one_drive_user_list" in value:
        import capo_kendra.types.one_drive_user_list

        out["OneDriveUserList"] = (
            capo_kendra.types.one_drive_user_list.serialize_aws_json_1_1(
                value["one_drive_user_list"]
            )
        )
    if "one_drive_user_s3_path" in value:
        import capo_kendra.types.s3_path

        out["OneDriveUserS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["one_drive_user_s3_path"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OneDriveUsers:
    out: OneDriveUsers = {}  # type: ignore[typeddict-item]
    if "OneDriveUserList" in data:
        import capo_kendra.types.one_drive_user_list

        out["one_drive_user_list"] = (
            capo_kendra.types.one_drive_user_list.deserialize_aws_json_1_1(
                data["OneDriveUserList"]
            )
        )
    if "OneDriveUserS3Path" in data:
        import capo_kendra.types.s3_path

        out["one_drive_user_s3_path"] = (
            capo_kendra.types.s3_path.deserialize_aws_json_1_1(
                data["OneDriveUserS3Path"]
            )
        )
    return out
