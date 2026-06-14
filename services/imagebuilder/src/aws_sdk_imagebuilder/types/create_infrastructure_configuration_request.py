"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateInfrastructureConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.instance_metadata_options
    import aws_sdk_imagebuilder.types.instance_profile_name_type
    import aws_sdk_imagebuilder.types.instance_type_list
    import aws_sdk_imagebuilder.types.logging
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean
    import aws_sdk_imagebuilder.types.placement
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.resource_tag_map
    import aws_sdk_imagebuilder.types.security_group_ids
    import aws_sdk_imagebuilder.types.sns_topic_arn
    import aws_sdk_imagebuilder.types.tag_map


class CreateInfrastructureConfigurationRequest(TypedDict):
    name: "aws_sdk_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the infrastructure configuration.</p>"""
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
    """<p>The subnet ID in which to place the instance used to customize your Amazon EC2 AMI.</p>"""
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
    """<p>The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs.</p>"""
    instance_metadata_options: NotRequired[
        "aws_sdk_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances.</p>"""
    tags: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.</p>"""
    placement: NotRequired["aws_sdk_imagebuilder.types.placement.Placement"]
    """<p>The instance placement settings that define where the instances that are launched from your image will run.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInfrastructureConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    if "tags" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "placement" in value:
        import aws_sdk_imagebuilder.types.placement

        out["placement"] = aws_sdk_imagebuilder.types.placement.serialize_json(
            value["placement"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateInfrastructureConfigurationRequest:
    out: CreateInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateInfrastructureConfigurationRequest.name required"
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
            "CreateInfrastructureConfigurationRequest.instance_profile_name required"
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
    if "tags" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tags"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "placement" in data:
        import aws_sdk_imagebuilder.types.placement

        out["placement"] = aws_sdk_imagebuilder.types.placement.deserialize_json(
            data["placement"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateInfrastructureConfigurationRequest.client_token required"
        )
    return out
