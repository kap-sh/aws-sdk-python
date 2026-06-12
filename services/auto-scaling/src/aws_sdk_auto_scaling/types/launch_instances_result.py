"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.client_token
    import aws_sdk_auto_scaling.types.instance_collections
    import aws_sdk_auto_scaling.types.launch_instances_errors
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class LaunchInstancesResult(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p> The name of the Auto Scaling group where the instances were launched. </p>"""
    client_token: NotRequired["aws_sdk_auto_scaling.types.client_token.ClientToken"]
    """<p> The idempotency token used for the request, either customer-specified or auto-generated. </p>"""
    instances: NotRequired[
        "aws_sdk_auto_scaling.types.instance_collections.InstanceCollections"
    ]
    """<p> A list of successfully launched instances including details such as instance type, Availability Zone, subnet, lifecycle state, and instance IDs. </p>"""
    errors: NotRequired[
        "aws_sdk_auto_scaling.types.launch_instances_errors.LaunchInstancesErrors"
    ]
    """<p> A list of errors encountered during the launch attempt including details about failed instance launches with their corresponding error codes and messages. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "instances" in value:
        import aws_sdk_auto_scaling.types.instance_collections

        aws_sdk_auto_scaling.types.instance_collections.serialize_query(
            value["instances"], pairs, f"{prefix}.Instances"
        )
    if "errors" in value:
        import aws_sdk_auto_scaling.types.launch_instances_errors

        aws_sdk_auto_scaling.types.launch_instances_errors.serialize_query(
            value["errors"], pairs, f"{prefix}.Errors"
        )


def deserialize_query(el: Element) -> LaunchInstancesResult:
    out: LaunchInstancesResult = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instances = el.find("Instances")
    if child_instances is not None:
        import aws_sdk_auto_scaling.types.instance_collections

        out["instances"] = (
            aws_sdk_auto_scaling.types.instance_collections.deserialize_query(
                child_instances
            )
        )
    child_errors = el.find("Errors")
    if child_errors is not None:
        import aws_sdk_auto_scaling.types.launch_instances_errors

        out["errors"] = (
            aws_sdk_auto_scaling.types.launch_instances_errors.deserialize_query(
                child_errors
            )
        )
    return out
