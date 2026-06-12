"""Generated from Smithy shape ``com.amazonaws.sagemaker#UnifiedStudioSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.account_id
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.region_name
    import aws_sdk_sagemaker.types.s3_uri
    import aws_sdk_sagemaker.types.single_sign_on_application_arn
    import aws_sdk_sagemaker.types.unified_studio_domain_id
    import aws_sdk_sagemaker.types.unified_studio_environment_id
    import aws_sdk_sagemaker.types.unified_studio_project_id


class UnifiedStudioSettings(TypedDict):
    studio_web_portal_access: NotRequired[
        "aws_sdk_sagemaker.types.feature_status.FeatureStatus"
    ]
    """<p>Sets whether you can access the domain in Amazon SageMaker Studio:</p> <dl> <dt>ENABLED</dt> <dd> <p>You can access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it in both studio interfaces.</p> </dd> <dt>DISABLED</dt> <dd> <p>You can't access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it only in that studio interface.</p> </dd> </dl> <p>To migrate a domain to Amazon SageMaker Unified Studio, you specify the UnifiedStudioSettings data type when you use the UpdateDomain action.</p>"""
    domain_account_id: NotRequired["aws_sdk_sagemaker.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that has the Amazon SageMaker Unified Studio domain. The default value, if you don't specify an ID, is the ID of the account that has the Amazon SageMaker AI domain.</p>"""
    domain_region: NotRequired["aws_sdk_sagemaker.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the domain is located in Amazon SageMaker Unified Studio. The default value, if you don't specify a Region, is the Region where the Amazon SageMaker AI domain is located.</p>"""
    domain_id: NotRequired[
        "aws_sdk_sagemaker.types.unified_studio_domain_id.UnifiedStudioDomainId"
    ]
    """<p>The ID of the Amazon SageMaker Unified Studio domain associated with this domain.</p>"""
    project_id: NotRequired[
        "aws_sdk_sagemaker.types.unified_studio_project_id.UnifiedStudioProjectId"
    ]
    """<p>The ID of the Amazon SageMaker Unified Studio project that corresponds to the domain.</p>"""
    environment_id: NotRequired[
        "aws_sdk_sagemaker.types.unified_studio_environment_id.UnifiedStudioEnvironmentId"
    ]
    """<p>The ID of the environment that Amazon SageMaker Unified Studio associates with the domain.</p>"""
    project_s3_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The location where Amazon S3 stores temporary execution data and other artifacts for the project that corresponds to the domain.</p>"""
    single_sign_on_application_arn: NotRequired[
        "aws_sdk_sagemaker.types.single_sign_on_application_arn.SingleSignOnApplicationArn"
    ]
    """<p>The ARN of the Amazon DataZone application managed by Amazon SageMaker Unified Studio in the Amazon Web Services IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnifiedStudioSettings) -> dict:
    out: dict = {}
    if "studio_web_portal_access" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["StudioWebPortalAccess"] = (
            aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["studio_web_portal_access"]
            )
        )
    if "domain_account_id" in value:
        out["DomainAccountId"] = value["domain_account_id"]
    if "domain_region" in value:
        out["DomainRegion"] = value["domain_region"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "project_id" in value:
        out["ProjectId"] = value["project_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "project_s3_path" in value:
        out["ProjectS3Path"] = value["project_s3_path"]
    if "single_sign_on_application_arn" in value:
        out["SingleSignOnApplicationArn"] = value["single_sign_on_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnifiedStudioSettings:
    out: UnifiedStudioSettings = {}  # type: ignore[typeddict-item]
    if "StudioWebPortalAccess" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["studio_web_portal_access"] = (
            aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["StudioWebPortalAccess"]
            )
        )
    if "DomainAccountId" in data:
        out["domain_account_id"] = data["DomainAccountId"]
    if "DomainRegion" in data:
        out["domain_region"] = data["DomainRegion"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "ProjectId" in data:
        out["project_id"] = data["ProjectId"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "ProjectS3Path" in data:
        out["project_s3_path"] = data["ProjectS3Path"]
    if "SingleSignOnApplicationArn" in data:
        out["single_sign_on_application_arn"] = data["SingleSignOnApplicationArn"]
    return out
