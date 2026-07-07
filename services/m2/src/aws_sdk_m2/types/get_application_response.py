"""Generated from Smithy shape ``com.amazonaws.m2#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_lifecycle
    import aws_sdk_m2.types.application_version_summary
    import aws_sdk_m2.types.arn
    import aws_sdk_m2.types.arn_list
    import aws_sdk_m2.types.deployed_version_summary
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.entity_description
    import aws_sdk_m2.types.entity_name
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.log_group_summaries
    import aws_sdk_m2.types.port_list
    import aws_sdk_m2.types.string100
    import aws_sdk_m2.types.tag_map
    import aws_sdk_m2.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    name: "aws_sdk_m2.types.entity_name.EntityName"
    """<p>The unique identifier of the application.</p>"""
    description: NotRequired["aws_sdk_m2.types.entity_description.EntityDescription"]
    """<p>The description of the application.</p>"""
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""
    application_arn: "aws_sdk_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    status: "aws_sdk_m2.types.application_lifecycle.ApplicationLifecycle"
    """<p>The status of the application.</p>"""
    latest_version: (
        "aws_sdk_m2.types.application_version_summary.ApplicationVersionSummary"
    )
    """<p>The latest version of the application.</p>"""
    deployed_version: NotRequired[
        "aws_sdk_m2.types.deployed_version_summary.DeployedVersionSummary"
    ]
    """<p>The version of the application that is deployed.</p>"""
    engine_type: "aws_sdk_m2.types.engine_type.EngineType"
    """<p>The type of the target platform for the application.</p>"""
    log_groups: NotRequired["aws_sdk_m2.types.log_group_summaries.LogGroupSummaries"]
    """<p>The list of log summaries. Each log summary includes the log type as well as the log group identifier. These are CloudWatch logs. Amazon Web Services Mainframe Modernization pushes the application log to CloudWatch under the customer's account.</p>"""
    creation_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when this application was created.</p>"""
    last_start_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when you last started the application. Null until the application runs for the first time.</p>"""
    tags: NotRequired["aws_sdk_m2.types.tag_map.TagMap"]
    """<p>A list of tags associated with the application.</p>"""
    environment_id: NotRequired["aws_sdk_m2.types.identifier.Identifier"]
    """<p>The identifier of the runtime environment where you want to deploy the application.</p>"""
    target_group_arns: NotRequired["aws_sdk_m2.types.arn_list.ArnList"]
    """<p>Returns the Amazon Resource Names (ARNs) of the target groups that are attached to the network load balancer.</p>"""
    listener_arns: NotRequired["aws_sdk_m2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Name (ARN) for the network load balancer listener created in your Amazon Web Services account. Amazon Web Services Mainframe Modernization creates this listener for you the first time you deploy an application.</p>"""
    listener_ports: NotRequired["aws_sdk_m2.types.port_list.PortList"]
    """<p>The port associated with the network load balancer listener created in your Amazon Web Services account.</p>"""
    load_balancer_dns_name: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The public DNS name of the load balancer created in your Amazon Web Services account.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The identifier of a customer managed key.</p>"""
    role_arn: NotRequired["aws_sdk_m2.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role associated with the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["applicationId"] = value["application_id"]
    out["applicationArn"] = value["application_arn"]
    out["status"] = value["status"]
    import aws_sdk_m2.types.application_version_summary

    out["latestVersion"] = aws_sdk_m2.types.application_version_summary.serialize_json(
        value["latest_version"]
    )
    if "deployed_version" in value:
        import aws_sdk_m2.types.deployed_version_summary

        out["deployedVersion"] = (
            aws_sdk_m2.types.deployed_version_summary.serialize_json(
                value["deployed_version"]
            )
        )
    out["engineType"] = value["engine_type"]
    if "log_groups" in value:
        import aws_sdk_m2.types.log_group_summaries

        out["logGroups"] = aws_sdk_m2.types.log_group_summaries.serialize_json(
            value["log_groups"]
        )
    import aws_sdk_m2.types.timestamp

    out["creationTime"] = aws_sdk_m2.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_start_time" in value:
        import aws_sdk_m2.types.timestamp

        out["lastStartTime"] = aws_sdk_m2.types.timestamp.serialize_json(
            value["last_start_time"]
        )
    if "tags" in value:
        import aws_sdk_m2.types.tag_map

        out["tags"] = aws_sdk_m2.types.tag_map.serialize_json(value["tags"])
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "target_group_arns" in value:
        import aws_sdk_m2.types.arn_list

        out["targetGroupArns"] = aws_sdk_m2.types.arn_list.serialize_json(
            value["target_group_arns"]
        )
    if "listener_arns" in value:
        import aws_sdk_m2.types.arn_list

        out["listenerArns"] = aws_sdk_m2.types.arn_list.serialize_json(
            value["listener_arns"]
        )
    if "listener_ports" in value:
        import aws_sdk_m2.types.port_list

        out["listenerPorts"] = aws_sdk_m2.types.port_list.serialize_json(
            value["listener_ports"]
        )
    if "load_balancer_dns_name" in value:
        out["loadBalancerDnsName"] = value["load_balancer_dns_name"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetApplicationResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("GetApplicationResponse.application_id required")
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("GetApplicationResponse.application_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetApplicationResponse.status required")
    if "latestVersion" in data:
        import aws_sdk_m2.types.application_version_summary

        out["latest_version"] = (
            aws_sdk_m2.types.application_version_summary.deserialize_json(
                data["latestVersion"]
            )
        )
    else:
        raise DeserializationError("GetApplicationResponse.latest_version required")
    if "deployedVersion" in data:
        import aws_sdk_m2.types.deployed_version_summary

        out["deployed_version"] = (
            aws_sdk_m2.types.deployed_version_summary.deserialize_json(
                data["deployedVersion"]
            )
        )
    if "engineType" in data:
        out["engine_type"] = data["engineType"]
    else:
        raise DeserializationError("GetApplicationResponse.engine_type required")
    if "logGroups" in data:
        import aws_sdk_m2.types.log_group_summaries

        out["log_groups"] = aws_sdk_m2.types.log_group_summaries.deserialize_json(
            data["logGroups"]
        )
    if "creationTime" in data:
        import aws_sdk_m2.types.timestamp

        out["creation_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetApplicationResponse.creation_time required")
    if "lastStartTime" in data:
        import aws_sdk_m2.types.timestamp

        out["last_start_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["lastStartTime"]
        )
    if "tags" in data:
        import aws_sdk_m2.types.tag_map

        out["tags"] = aws_sdk_m2.types.tag_map.deserialize_json(data["tags"])
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "targetGroupArns" in data:
        import aws_sdk_m2.types.arn_list

        out["target_group_arns"] = aws_sdk_m2.types.arn_list.deserialize_json(
            data["targetGroupArns"]
        )
    if "listenerArns" in data:
        import aws_sdk_m2.types.arn_list

        out["listener_arns"] = aws_sdk_m2.types.arn_list.deserialize_json(
            data["listenerArns"]
        )
    if "listenerPorts" in data:
        import aws_sdk_m2.types.port_list

        out["listener_ports"] = aws_sdk_m2.types.port_list.deserialize_json(
            data["listenerPorts"]
        )
    if "loadBalancerDnsName" in data:
        out["load_balancer_dns_name"] = data["loadBalancerDnsName"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
