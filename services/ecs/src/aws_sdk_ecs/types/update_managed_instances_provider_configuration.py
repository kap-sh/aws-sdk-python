"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateManagedInstancesProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_configuration
    import aws_sdk_ecs.types.infrastructure_optimization
    import aws_sdk_ecs.types.instance_launch_template_update
    import aws_sdk_ecs.types.propagate_mi_tags
    import aws_sdk_ecs.types.string


class UpdateManagedInstancesProviderConfiguration(TypedDict):
    infrastructure_role_arn: "aws_sdk_ecs.types.string.String"
    r"""<p>The updated Amazon Resource Name (ARN) of the infrastructure role. The new role must have the necessary permissions to manage instances and access required Amazon Web Services services.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html\">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    instance_launch_template: (
        "aws_sdk_ecs.types.instance_launch_template_update.InstanceLaunchTemplateUpdate"
    )
    """<p>The updated launch template configuration. Changes to the launch template affect new instances launched after the update, while existing instances continue to use their original configuration.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>The updated tag propagation setting. When changed, this affects only new instances launched after the update.</p>"""
    infrastructure_optimization: NotRequired[
        "aws_sdk_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>The updated infrastructure optimization configuration. Changes to this setting affect how Amazon ECS optimizes instances going forward.</p>"""
    auto_repair_configuration: NotRequired[
        "aws_sdk_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The updated auto repair configuration for the Amazon ECS Managed Instances capacity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateManagedInstancesProviderConfiguration) -> dict:
    out: dict = {}
    out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    import aws_sdk_ecs.types.instance_launch_template_update

    out["instanceLaunchTemplate"] = (
        aws_sdk_ecs.types.instance_launch_template_update.serialize_aws_json_1_1(
            value["instance_launch_template"]
        )
    )
    if "propagate_tags" in value:
        import aws_sdk_ecs.types.propagate_mi_tags

        out["propagateTags"] = (
            aws_sdk_ecs.types.propagate_mi_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    if "infrastructure_optimization" in value:
        import aws_sdk_ecs.types.infrastructure_optimization

        out["infrastructureOptimization"] = (
            aws_sdk_ecs.types.infrastructure_optimization.serialize_aws_json_1_1(
                value["infrastructure_optimization"]
            )
        )
    if "auto_repair_configuration" in value:
        import aws_sdk_ecs.types.auto_repair_configuration

        out["autoRepairConfiguration"] = (
            aws_sdk_ecs.types.auto_repair_configuration.serialize_aws_json_1_1(
                value["auto_repair_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateManagedInstancesProviderConfiguration:
    out: UpdateManagedInstancesProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "infrastructureRoleArn" in data:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    else:
        raise DeserializationError(
            "UpdateManagedInstancesProviderConfiguration.infrastructure_role_arn required"
        )
    if "instanceLaunchTemplate" in data:
        import aws_sdk_ecs.types.instance_launch_template_update

        out["instance_launch_template"] = (
            aws_sdk_ecs.types.instance_launch_template_update.deserialize_aws_json_1_1(
                data["instanceLaunchTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateManagedInstancesProviderConfiguration.instance_launch_template required"
        )
    if "propagateTags" in data:
        import aws_sdk_ecs.types.propagate_mi_tags

        out["propagate_tags"] = (
            aws_sdk_ecs.types.propagate_mi_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    if "infrastructureOptimization" in data:
        import aws_sdk_ecs.types.infrastructure_optimization

        out["infrastructure_optimization"] = (
            aws_sdk_ecs.types.infrastructure_optimization.deserialize_aws_json_1_1(
                data["infrastructureOptimization"]
            )
        )
    if "autoRepairConfiguration" in data:
        import aws_sdk_ecs.types.auto_repair_configuration

        out["auto_repair_configuration"] = (
            aws_sdk_ecs.types.auto_repair_configuration.deserialize_aws_json_1_1(
                data["autoRepairConfiguration"]
            )
        )
    return out
