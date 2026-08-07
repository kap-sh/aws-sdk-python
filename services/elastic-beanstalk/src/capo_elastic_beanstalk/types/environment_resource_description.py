"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentResourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.auto_scaling_group_list
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.instance_list
    import capo_elastic_beanstalk.types.launch_configuration_list
    import capo_elastic_beanstalk.types.launch_template_list
    import capo_elastic_beanstalk.types.load_balancer_list
    import capo_elastic_beanstalk.types.queue_list
    import capo_elastic_beanstalk.types.trigger_list


class EnvironmentResourceDescription(TypedDict, closed=True):
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment.</p>"""
    auto_scaling_groups: NotRequired[
        "capo_elastic_beanstalk.types.auto_scaling_group_list.AutoScalingGroupList"
    ]
    """<p> The <code>AutoScalingGroups</code> used by this environment. </p>"""
    instances: NotRequired["capo_elastic_beanstalk.types.instance_list.InstanceList"]
    """<p>The Amazon EC2 instances used by this environment.</p>"""
    launch_configurations: NotRequired[
        "capo_elastic_beanstalk.types.launch_configuration_list.LaunchConfigurationList"
    ]
    """<p>The Auto Scaling launch configurations in use by this environment.</p>"""
    launch_templates: NotRequired[
        "capo_elastic_beanstalk.types.launch_template_list.LaunchTemplateList"
    ]
    """<p>The Amazon EC2 launch templates in use by this environment.</p>"""
    load_balancers: NotRequired[
        "capo_elastic_beanstalk.types.load_balancer_list.LoadBalancerList"
    ]
    """<p>The LoadBalancers in use by this environment.</p>"""
    triggers: NotRequired["capo_elastic_beanstalk.types.trigger_list.TriggerList"]
    """<p>The <code>AutoScaling</code> triggers in use by this environment. </p>"""
    queues: NotRequired["capo_elastic_beanstalk.types.queue_list.QueueList"]
    """<p>The queues used by this environment.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentResourceDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "auto_scaling_groups" in value:
        import capo_elastic_beanstalk.types.auto_scaling_group_list

        capo_elastic_beanstalk.types.auto_scaling_group_list.serialize_query(
            value["auto_scaling_groups"], pairs, f"{key_prefix}AutoScalingGroups"
        )
    if "instances" in value:
        import capo_elastic_beanstalk.types.instance_list

        capo_elastic_beanstalk.types.instance_list.serialize_query(
            value["instances"], pairs, f"{key_prefix}Instances"
        )
    if "launch_configurations" in value:
        import capo_elastic_beanstalk.types.launch_configuration_list

        capo_elastic_beanstalk.types.launch_configuration_list.serialize_query(
            value["launch_configurations"], pairs, f"{key_prefix}LaunchConfigurations"
        )
    if "launch_templates" in value:
        import capo_elastic_beanstalk.types.launch_template_list

        capo_elastic_beanstalk.types.launch_template_list.serialize_query(
            value["launch_templates"], pairs, f"{key_prefix}LaunchTemplates"
        )
    if "load_balancers" in value:
        import capo_elastic_beanstalk.types.load_balancer_list

        capo_elastic_beanstalk.types.load_balancer_list.serialize_query(
            value["load_balancers"], pairs, f"{key_prefix}LoadBalancers"
        )
    if "triggers" in value:
        import capo_elastic_beanstalk.types.trigger_list

        capo_elastic_beanstalk.types.trigger_list.serialize_query(
            value["triggers"], pairs, f"{key_prefix}Triggers"
        )
    if "queues" in value:
        import capo_elastic_beanstalk.types.queue_list

        capo_elastic_beanstalk.types.queue_list.serialize_query(
            value["queues"], pairs, f"{key_prefix}Queues"
        )


def deserialize_query(el: Element) -> EnvironmentResourceDescription:
    out: EnvironmentResourceDescription = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_auto_scaling_groups = el.find("AutoScalingGroups")
    if child_auto_scaling_groups is not None:
        import capo_elastic_beanstalk.types.auto_scaling_group_list

        out["auto_scaling_groups"] = (
            capo_elastic_beanstalk.types.auto_scaling_group_list.deserialize_query(
                child_auto_scaling_groups
            )
        )
    child_instances = el.find("Instances")
    if child_instances is not None:
        import capo_elastic_beanstalk.types.instance_list

        out["instances"] = capo_elastic_beanstalk.types.instance_list.deserialize_query(
            child_instances
        )
    child_launch_configurations = el.find("LaunchConfigurations")
    if child_launch_configurations is not None:
        import capo_elastic_beanstalk.types.launch_configuration_list

        out["launch_configurations"] = (
            capo_elastic_beanstalk.types.launch_configuration_list.deserialize_query(
                child_launch_configurations
            )
        )
    child_launch_templates = el.find("LaunchTemplates")
    if child_launch_templates is not None:
        import capo_elastic_beanstalk.types.launch_template_list

        out["launch_templates"] = (
            capo_elastic_beanstalk.types.launch_template_list.deserialize_query(
                child_launch_templates
            )
        )
    child_load_balancers = el.find("LoadBalancers")
    if child_load_balancers is not None:
        import capo_elastic_beanstalk.types.load_balancer_list

        out["load_balancers"] = (
            capo_elastic_beanstalk.types.load_balancer_list.deserialize_query(
                child_load_balancers
            )
        )
    child_triggers = el.find("Triggers")
    if child_triggers is not None:
        import capo_elastic_beanstalk.types.trigger_list

        out["triggers"] = capo_elastic_beanstalk.types.trigger_list.deserialize_query(
            child_triggers
        )
    child_queues = el.find("Queues")
    if child_queues is not None:
        import capo_elastic_beanstalk.types.queue_list

        out["queues"] = capo_elastic_beanstalk.types.queue_list.deserialize_query(
            child_queues
        )
    return out
