"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateInfrastructureConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.infrastructure_configuration_arn
    import aws_sdk_imagebuilder.types.instance_metadata_options
    import aws_sdk_imagebuilder.types.instance_profile_name_type
    import aws_sdk_imagebuilder.types.instance_type_list
    import aws_sdk_imagebuilder.types.logging
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.placement
    import aws_sdk_imagebuilder.types.resource_tag_map
    import aws_sdk_imagebuilder.types.security_group_ids
    import aws_sdk_imagebuilder.types.sns_topic_arn


class UpdateInfrastructureConfigurationRequest(TypedDict):
    infrastructure_configuration_arn: "aws_sdk_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the infrastructure configuration.</p>"""
    instance_types: NotRequired[
        "aws_sdk_imagebuilder.types.instance_type_list.InstanceTypeList"
    ]
    """<p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.</p>"""
    instance_profile_name: (
        "aws_sdk_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType"
    )
    """<p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_imagebuilder.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>"""
    subnet_id: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The subnet ID to place the instance used to customize your Amazon EC2 AMI in.</p>"""
    logging: NotRequired["aws_sdk_imagebuilder.types.logging.Logging"]
    """<p>The logging configuration of the infrastructure configuration.</p>"""
    key_pair: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>"""
    terminate_instance_on_failure: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_imagebuilder.types.sns_topic_arn.SnsTopicArn"]
    """<p>The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.</p> <note> <p>EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.</p> </note>"""
    resource_tags: NotRequired[
        "aws_sdk_imagebuilder.types.resource_tag_map.ResourceTagMap"
    ]
    """<p>The tags attached to the resource created by Image Builder.</p>"""
    instance_metadata_options: NotRequired[
        "aws_sdk_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances. For more information about instance metadata options, see one of the following links:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html\">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i> for Linux instances.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html\">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i> for Windows instances.</p> </li> </ul>"""
    placement: NotRequired["aws_sdk_imagebuilder.types.placement.Placement"]
    """<p>The instance placement settings that define where the instances that are launched from your image will run.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInfrastructureConfigurationRequest) -> dict:
    out: dict = {}
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "instance_types" in value:
        import aws_sdk_imagebuilder.types.instance_type_list

        out["instanceTypes"] = (
            aws_sdk_imagebuilder.types.instance_type_list.serialize_json(
                value["instance_types"]
            )
        )
    out["instanceProfileName"] = value["instance_profile_name"]
    if "security_group_ids" in value:
        import aws_sdk_imagebuilder.types.security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_imagebuilder.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "logging" in value:
        import aws_sdk_imagebuilder.types.logging

        out["logging"] = aws_sdk_imagebuilder.types.logging.serialize_json(
            value["logging"]
        )
    if "key_pair" in value:
        out["keyPair"] = value["key_pair"]
    if "terminate_instance_on_failure" in value:
        out["terminateInstanceOnFailure"] = value["terminate_instance_on_failure"]
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    if "resource_tags" in value:
        import aws_sdk_imagebuilder.types.resource_tag_map

        out["resourceTags"] = (
            aws_sdk_imagebuilder.types.resource_tag_map.serialize_json(
                value["resource_tags"]
            )
        )
    if "instance_metadata_options" in value:
        import aws_sdk_imagebuilder.types.instance_metadata_options

        out["instanceMetadataOptions"] = (
            aws_sdk_imagebuilder.types.instance_metadata_options.serialize_json(
                value["instance_metadata_options"]
            )
        )
    if "placement" in value:
        import aws_sdk_imagebuilder.types.placement

        out["placement"] = aws_sdk_imagebuilder.types.placement.serialize_json(
            value["placement"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateInfrastructureConfigurationRequest:
    out: UpdateInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "infrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateInfrastructureConfigurationRequest.infrastructure_configuration_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "instanceTypes" in data:
        import aws_sdk_imagebuilder.types.instance_type_list

        out["instance_types"] = (
            aws_sdk_imagebuilder.types.instance_type_list.deserialize_json(
                data["instanceTypes"]
            )
        )
    if "instanceProfileName" in data:
        out["instance_profile_name"] = data["instanceProfileName"]
    else:
        raise DeserializationError(
            "UpdateInfrastructureConfigurationRequest.instance_profile_name required"
        )
    if "securityGroupIds" in data:
        import aws_sdk_imagebuilder.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_imagebuilder.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "logging" in data:
        import aws_sdk_imagebuilder.types.logging

        out["logging"] = aws_sdk_imagebuilder.types.logging.deserialize_json(
            data["logging"]
        )
    if "keyPair" in data:
        out["key_pair"] = data["keyPair"]
    if "terminateInstanceOnFailure" in data:
        out["terminate_instance_on_failure"] = data["terminateInstanceOnFailure"]
    if "snsTopicArn" in data:
        out["sns_topic_arn"] = data["snsTopicArn"]
    if "resourceTags" in data:
        import aws_sdk_imagebuilder.types.resource_tag_map

        out["resource_tags"] = (
            aws_sdk_imagebuilder.types.resource_tag_map.deserialize_json(
                data["resourceTags"]
            )
        )
    if "instanceMetadataOptions" in data:
        import aws_sdk_imagebuilder.types.instance_metadata_options

        out["instance_metadata_options"] = (
            aws_sdk_imagebuilder.types.instance_metadata_options.deserialize_json(
                data["instanceMetadataOptions"]
            )
        )
    if "placement" in data:
        import aws_sdk_imagebuilder.types.placement

        out["placement"] = aws_sdk_imagebuilder.types.placement.deserialize_json(
            data["placement"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "UpdateInfrastructureConfigurationRequest.client_token required"
        )
    return out
