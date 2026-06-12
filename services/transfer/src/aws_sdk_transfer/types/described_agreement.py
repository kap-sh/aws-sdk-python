"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedAgreement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.agreement_id
    import aws_sdk_transfer.types.agreement_status_type
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.custom_directories_type
    import aws_sdk_transfer.types.description
    import aws_sdk_transfer.types.enforce_message_signing_type
    import aws_sdk_transfer.types.home_directory
    import aws_sdk_transfer.types.preserve_filename_type
    import aws_sdk_transfer.types.profile_id
    import aws_sdk_transfer.types.role
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.tags


class DescribedAgreement(TypedDict):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the agreement.</p>"""
    agreement_id: NotRequired["aws_sdk_transfer.types.agreement_id.AgreementId"]
    """<p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>"""
    description: NotRequired["aws_sdk_transfer.types.description.Description"]
    """<p>The name or short description that's used to identify the agreement.</p>"""
    status: NotRequired[
        "aws_sdk_transfer.types.agreement_status_type.AgreementStatusType"
    ]
    """<p>The current status of the agreement, either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    server_id: NotRequired["aws_sdk_transfer.types.server_id.ServerId"]
    """<p>A system-assigned unique identifier for a server instance. This identifier indicates the specific server that the agreement uses.</p>"""
    local_profile_id: NotRequired["aws_sdk_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the AS2 local profile.</p>"""
    partner_profile_id: NotRequired["aws_sdk_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the partner profile used in the agreement.</p>"""
    base_directory: NotRequired["aws_sdk_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for files that are transferred by using the AS2 protocol.</p>"""
    access_role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for agreements.</p>"""
    preserve_filename: NotRequired[
        "aws_sdk_transfer.types.preserve_filename_type.PreserveFilenameType"
    ]
    """<p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2\">File names and locations</a>.</p> </li> </ul>"""
    enforce_message_signing: NotRequired[
        "aws_sdk_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
    ]
    """<p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>"""
    custom_directories: NotRequired[
        "aws_sdk_transfer.types.custom_directories_type.CustomDirectoriesType"
    ]
    """<p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedAgreement) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "agreement_id" in value:
        out["AgreementId"] = value["agreement_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_transfer.types.agreement_status_type

        out["Status"] = (
            aws_sdk_transfer.types.agreement_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "server_id" in value:
        out["ServerId"] = value["server_id"]
    if "local_profile_id" in value:
        out["LocalProfileId"] = value["local_profile_id"]
    if "partner_profile_id" in value:
        out["PartnerProfileId"] = value["partner_profile_id"]
    if "base_directory" in value:
        out["BaseDirectory"] = value["base_directory"]
    if "access_role" in value:
        out["AccessRole"] = value["access_role"]
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "preserve_filename" in value:
        import aws_sdk_transfer.types.preserve_filename_type

        out["PreserveFilename"] = (
            aws_sdk_transfer.types.preserve_filename_type.serialize_aws_json_1_1(
                value["preserve_filename"]
            )
        )
    if "enforce_message_signing" in value:
        import aws_sdk_transfer.types.enforce_message_signing_type

        out["EnforceMessageSigning"] = (
            aws_sdk_transfer.types.enforce_message_signing_type.serialize_aws_json_1_1(
                value["enforce_message_signing"]
            )
        )
    if "custom_directories" in value:
        import aws_sdk_transfer.types.custom_directories_type

        out["CustomDirectories"] = (
            aws_sdk_transfer.types.custom_directories_type.serialize_aws_json_1_1(
                value["custom_directories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedAgreement:
    out: DescribedAgreement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedAgreement.arn required")
    if "AgreementId" in data:
        out["agreement_id"] = data["AgreementId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_transfer.types.agreement_status_type

        out["status"] = (
            aws_sdk_transfer.types.agreement_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    if "LocalProfileId" in data:
        out["local_profile_id"] = data["LocalProfileId"]
    if "PartnerProfileId" in data:
        out["partner_profile_id"] = data["PartnerProfileId"]
    if "BaseDirectory" in data:
        out["base_directory"] = data["BaseDirectory"]
    if "AccessRole" in data:
        out["access_role"] = data["AccessRole"]
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "PreserveFilename" in data:
        import aws_sdk_transfer.types.preserve_filename_type

        out["preserve_filename"] = (
            aws_sdk_transfer.types.preserve_filename_type.deserialize_aws_json_1_1(
                data["PreserveFilename"]
            )
        )
    if "EnforceMessageSigning" in data:
        import aws_sdk_transfer.types.enforce_message_signing_type

        out["enforce_message_signing"] = (
            aws_sdk_transfer.types.enforce_message_signing_type.deserialize_aws_json_1_1(
                data["EnforceMessageSigning"]
            )
        )
    if "CustomDirectories" in data:
        import aws_sdk_transfer.types.custom_directories_type

        out["custom_directories"] = (
            aws_sdk_transfer.types.custom_directories_type.deserialize_aws_json_1_1(
                data["CustomDirectories"]
            )
        )
    return out
