"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.definition_document
    import aws_sdk_iotthingsgraph.types.dependency_revisions
    import aws_sdk_iotthingsgraph.types.metrics_configuration
    import aws_sdk_iotthingsgraph.types.role_arn
    import aws_sdk_iotthingsgraph.types.s3_bucket_name
    import aws_sdk_iotthingsgraph.types.system_instance_summary
    import aws_sdk_iotthingsgraph.types.version


class SystemInstanceDescription(TypedDict):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
    ]
    """<p>An object that contains summary information about a system instance.</p>"""
    definition: NotRequired[
        "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument"
    ]
    s3_bucket_name: NotRequired[
        "aws_sdk_iotthingsgraph.types.s3_bucket_name.S3BucketName"
    ]
    """<p>The Amazon Simple Storage Service bucket where information about a system instance is stored.</p>"""
    metrics_configuration: NotRequired[
        "aws_sdk_iotthingsgraph.types.metrics_configuration.MetricsConfiguration"
    ]
    validated_namespace_version: NotRequired[
        "aws_sdk_iotthingsgraph.types.version.Version"
    ]
    """<p>The version of the user's namespace against which the system instance was validated.</p>"""
    validated_dependency_revisions: NotRequired[
        "aws_sdk_iotthingsgraph.types.dependency_revisions.DependencyRevisions"
    ]
    """<p>A list of objects that contain all of the IDs and revision numbers of workflows and systems that are used in a system instance.</p>"""
    flow_actions_role_arn: NotRequired["aws_sdk_iotthingsgraph.types.role_arn.RoleArn"]
    """<p>The AWS Identity and Access Management (IAM) role that AWS IoT Things Graph assumes during flow execution in a cloud deployment. This role must have read and write permissionss to AWS Lambda and AWS IoT and to any other AWS services that the flow uses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceDescription) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    if "definition" in value:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "metrics_configuration" in value:
        import aws_sdk_iotthingsgraph.types.metrics_configuration

        out["metricsConfiguration"] = (
            aws_sdk_iotthingsgraph.types.metrics_configuration.serialize_aws_json_1_1(
                value["metrics_configuration"]
            )
        )
    if "validated_namespace_version" in value:
        out["validatedNamespaceVersion"] = value["validated_namespace_version"]
    if "validated_dependency_revisions" in value:
        import aws_sdk_iotthingsgraph.types.dependency_revisions

        out["validatedDependencyRevisions"] = (
            aws_sdk_iotthingsgraph.types.dependency_revisions.serialize_aws_json_1_1(
                value["validated_dependency_revisions"]
            )
        )
    if "flow_actions_role_arn" in value:
        out["flowActionsRoleArn"] = value["flow_actions_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemInstanceDescription:
    out: SystemInstanceDescription = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    if "definition" in data:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    if "metricsConfiguration" in data:
        import aws_sdk_iotthingsgraph.types.metrics_configuration

        out["metrics_configuration"] = (
            aws_sdk_iotthingsgraph.types.metrics_configuration.deserialize_aws_json_1_1(
                data["metricsConfiguration"]
            )
        )
    if "validatedNamespaceVersion" in data:
        out["validated_namespace_version"] = data["validatedNamespaceVersion"]
    if "validatedDependencyRevisions" in data:
        import aws_sdk_iotthingsgraph.types.dependency_revisions

        out["validated_dependency_revisions"] = (
            aws_sdk_iotthingsgraph.types.dependency_revisions.deserialize_aws_json_1_1(
                data["validatedDependencyRevisions"]
            )
        )
    if "flowActionsRoleArn" in data:
        out["flow_actions_role_arn"] = data["flowActionsRoleArn"]
    return out
