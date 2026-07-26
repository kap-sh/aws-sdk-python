"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.domain
    import capo_personalize.types.failure_reason
    import capo_personalize.types.kms_key_arn
    import capo_personalize.types.name
    import capo_personalize.types.role_arn
    import capo_personalize.types.status


class DatasetGroup(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the dataset group.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The current status of the dataset group.</p> <p>A dataset group can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING</p> </li> </ul>"""
    role_arn: NotRequired["capo_personalize.types.role_arn.RoleArn"]
    """<p>The ARN of the Identity and Access Management (IAM) role that has permissions to access the Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</p>"""
    kms_key_arn: NotRequired["capo_personalize.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key used to encrypt the datasets.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the dataset group.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The last update date and time (in Unix time) of the dataset group.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If creating a dataset group fails, provides the reason why.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p>The domain of a Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetGroup:
    out: DatasetGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "domain" in data:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
