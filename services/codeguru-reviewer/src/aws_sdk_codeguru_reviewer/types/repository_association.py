"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.arn
    import aws_sdk_codeguru_reviewer.types.association_id
    import aws_sdk_codeguru_reviewer.types.connection_arn
    import aws_sdk_codeguru_reviewer.types.kms_key_details
    import aws_sdk_codeguru_reviewer.types.name
    import aws_sdk_codeguru_reviewer.types.owner
    import aws_sdk_codeguru_reviewer.types.provider_type
    import aws_sdk_codeguru_reviewer.types.repository_association_state
    import aws_sdk_codeguru_reviewer.types.s3_repository_details
    import aws_sdk_codeguru_reviewer.types.state_reason
    import aws_sdk_codeguru_reviewer.types.time_stamp


class RepositoryAssociation(TypedDict):
    association_id: NotRequired[
        "aws_sdk_codeguru_reviewer.types.association_id.AssociationId"
    ]
    """<p>The ID of the repository association.</p>"""
    association_arn: NotRequired["aws_sdk_codeguru_reviewer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) identifying the repository association.</p>"""
    connection_arn: NotRequired[
        "aws_sdk_codeguru_reviewer.types.connection_arn.ConnectionArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of an Amazon Web Services CodeStar Connections connection. Its format is <code>arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id</code>. For more information, see <a href=\"https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html\">Connection</a> in the <i>Amazon Web Services CodeStar Connections API Reference</i>.</p>"""
    name: NotRequired["aws_sdk_codeguru_reviewer.types.name.Name"]
    """<p>The name of the repository.</p>"""
    owner: NotRequired["aws_sdk_codeguru_reviewer.types.owner.Owner"]
    """<p>The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.</p>"""
    provider_type: NotRequired[
        "aws_sdk_codeguru_reviewer.types.provider_type.ProviderType"
    ]
    """<p>The provider type of the repository association.</p>"""
    state: NotRequired[
        "aws_sdk_codeguru_reviewer.types.repository_association_state.RepositoryAssociationState"
    ]
    r"""<p>The state of the repository association.</p> <p>The valid repository association states are:</p> <ul> <li> <p> <b>Associated</b>: The repository association is complete.</p> </li> <li> <p> <b>Associating</b>: CodeGuru Reviewer is:</p> <ul> <li> <p>Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.</p> <note> <p>If your repository <code>ProviderType</code> is <code>GitHub</code>, <code>GitHub Enterprise Server</code>, or <code>Bitbucket</code>, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.</p> </note> </li> <li> <p>Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.</p> </li> </ul> </li> <li> <p> <b>Failed</b>: The repository failed to associate or disassociate.</p> </li> <li> <p> <b>Disassociating</b>: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.</p> </li> <li> <p> <b>Disassociated</b>: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html\">Using tags to control access to associated repositories</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p> </li> </ul>"""
    state_reason: NotRequired[
        "aws_sdk_codeguru_reviewer.types.state_reason.StateReason"
    ]
    """<p>A description of why the repository association is in the current state.</p>"""
    last_updated_time_stamp: NotRequired[
        "aws_sdk_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time, in milliseconds since the epoch, when the repository association was last updated.</p>"""
    created_time_stamp: NotRequired[
        "aws_sdk_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time, in milliseconds since the epoch, when the repository association was created.</p>"""
    kms_key_details: NotRequired[
        "aws_sdk_codeguru_reviewer.types.kms_key_details.KMSKeyDetails"
    ]
    """<p>A <code>KMSKeyDetails</code> object that contains:</p> <ul> <li> <p>The encryption option for this repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (<code>AWS_OWNED_CMK</code>) or customer managed (<code>CUSTOMER_MANAGED_CMK</code>).</p> </li> <li> <p>The ID of the Amazon Web Services KMS key that is associated with this repository association.</p> </li> </ul>"""
    s3_repository_details: NotRequired[
        "aws_sdk_codeguru_reviewer.types.s3_repository_details.S3RepositoryDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "association_arn" in value:
        out["AssociationArn"] = value["association_arn"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "provider_type" in value:
        import aws_sdk_codeguru_reviewer.types.provider_type

        out["ProviderType"] = (
            aws_sdk_codeguru_reviewer.types.provider_type.serialize_json(
                value["provider_type"]
            )
        )
    if "state" in value:
        import aws_sdk_codeguru_reviewer.types.repository_association_state

        out["State"] = (
            aws_sdk_codeguru_reviewer.types.repository_association_state.serialize_json(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "last_updated_time_stamp" in value:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["LastUpdatedTimeStamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.serialize_json(
                value["last_updated_time_stamp"]
            )
        )
    if "created_time_stamp" in value:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["CreatedTimeStamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.serialize_json(
                value["created_time_stamp"]
            )
        )
    if "kms_key_details" in value:
        import aws_sdk_codeguru_reviewer.types.kms_key_details

        out["KMSKeyDetails"] = (
            aws_sdk_codeguru_reviewer.types.kms_key_details.serialize_json(
                value["kms_key_details"]
            )
        )
    if "s3_repository_details" in value:
        import aws_sdk_codeguru_reviewer.types.s3_repository_details

        out["S3RepositoryDetails"] = (
            aws_sdk_codeguru_reviewer.types.s3_repository_details.serialize_json(
                value["s3_repository_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RepositoryAssociation:
    out: RepositoryAssociation = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "AssociationArn" in data:
        out["association_arn"] = data["AssociationArn"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "ProviderType" in data:
        import aws_sdk_codeguru_reviewer.types.provider_type

        out["provider_type"] = (
            aws_sdk_codeguru_reviewer.types.provider_type.deserialize_json(
                data["ProviderType"]
            )
        )
    if "State" in data:
        import aws_sdk_codeguru_reviewer.types.repository_association_state

        out["state"] = (
            aws_sdk_codeguru_reviewer.types.repository_association_state.deserialize_json(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "LastUpdatedTimeStamp" in data:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["last_updated_time_stamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["LastUpdatedTimeStamp"]
            )
        )
    if "CreatedTimeStamp" in data:
        import aws_sdk_codeguru_reviewer.types.time_stamp

        out["created_time_stamp"] = (
            aws_sdk_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["CreatedTimeStamp"]
            )
        )
    if "KMSKeyDetails" in data:
        import aws_sdk_codeguru_reviewer.types.kms_key_details

        out["kms_key_details"] = (
            aws_sdk_codeguru_reviewer.types.kms_key_details.deserialize_json(
                data["KMSKeyDetails"]
            )
        )
    if "S3RepositoryDetails" in data:
        import aws_sdk_codeguru_reviewer.types.s3_repository_details

        out["s3_repository_details"] = (
            aws_sdk_codeguru_reviewer.types.s3_repository_details.deserialize_json(
                data["S3RepositoryDetails"]
            )
        )
    return out
