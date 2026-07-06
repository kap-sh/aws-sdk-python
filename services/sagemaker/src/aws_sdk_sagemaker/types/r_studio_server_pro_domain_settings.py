"""Generated from Smithy shape ``com.amazonaws.sagemaker#RStudioServerProDomainSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_spec
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.string


class RStudioServerProDomainSettings(TypedDict, closed=True):
    domain_execution_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role for the <code>RStudioServerPro</code> Domain-level app.</p>"""
    r_studio_connect_url: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A URL pointing to an RStudio Connect server.</p>"""
    r_studio_package_manager_url: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A URL pointing to an RStudio Package Manager server.</p>"""
    default_resource_spec: NotRequired[
        "aws_sdk_sagemaker.types.resource_spec.ResourceSpec"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RStudioServerProDomainSettings) -> dict:
    out: dict = {}
    if "domain_execution_role_arn" in value:
        out["DomainExecutionRoleArn"] = value["domain_execution_role_arn"]
    if "r_studio_connect_url" in value:
        out["RStudioConnectUrl"] = value["r_studio_connect_url"]
    if "r_studio_package_manager_url" in value:
        out["RStudioPackageManagerUrl"] = value["r_studio_package_manager_url"]
    if "default_resource_spec" in value:
        import aws_sdk_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            aws_sdk_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RStudioServerProDomainSettings:
    out: RStudioServerProDomainSettings = {}  # type: ignore[typeddict-item]
    if "DomainExecutionRoleArn" in data:
        out["domain_execution_role_arn"] = data["DomainExecutionRoleArn"]
    if "RStudioConnectUrl" in data:
        out["r_studio_connect_url"] = data["RStudioConnectUrl"]
    if "RStudioPackageManagerUrl" in data:
        out["r_studio_package_manager_url"] = data["RStudioPackageManagerUrl"]
    if "DefaultResourceSpec" in data:
        import aws_sdk_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            aws_sdk_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    return out
