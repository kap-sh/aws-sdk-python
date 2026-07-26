"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InfrastructureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.instance_metadata_options
    import capo_imagebuilder.types.instance_profile_name_type
    import capo_imagebuilder.types.instance_type_list
    import capo_imagebuilder.types.logging
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.placement
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.resource_tag_map
    import capo_imagebuilder.types.security_group_ids
    import capo_imagebuilder.types.tag_map


class InfrastructureConfiguration(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the infrastructure configuration.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the infrastructure configuration.</p>"""
    instance_types: NotRequired[
        "capo_imagebuilder.types.instance_type_list.InstanceTypeList"
    ]
    """<p>The instance types of the infrastructure configuration.</p>"""
    instance_profile_name: NotRequired[
        "capo_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType"
    ]
    """<p>The instance profile of the infrastructure configuration.</p>"""
    security_group_ids: NotRequired[
        "capo_imagebuilder.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs of the infrastructure configuration.</p>"""
    subnet_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The subnet ID of the infrastructure configuration.</p>"""
    logging: NotRequired["capo_imagebuilder.types.logging.Logging"]
    """<p>The logging configuration of the infrastructure configuration.</p>"""
    key_pair: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon EC2 key pair of the infrastructure configuration.</p>"""
    terminate_instance_on_failure: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The terminate instance on failure configuration of the infrastructure configuration.</p>"""
    sns_topic_arn: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.</p> <note> <p>EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.</p> </note>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the infrastructure configuration was created.</p>"""
    date_updated: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which the infrastructure configuration was last updated.</p>"""
    resource_tags: NotRequired[
        "capo_imagebuilder.types.resource_tag_map.ResourceTagMap"
    ]
    """<p>The tags attached to the resource created by Image Builder.</p>"""
    instance_metadata_options: NotRequired[
        "capo_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The instance metadata option settings for the infrastructure configuration.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the infrastructure configuration.</p>"""
    placement: NotRequired["capo_imagebuilder.types.placement.Placement"]
    """<p>The instance placement settings that define where the instances that are launched from your image will run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "instance_types" in value:
        import capo_imagebuilder.types.instance_type_list

        out["instanceTypes"] = (
            capo_imagebuilder.types.instance_type_list.serialize_json(
                value["instance_types"]
            )
        )
    if "instance_profile_name" in value:
        out["instanceProfileName"] = value["instance_profile_name"]
    if "security_group_ids" in value:
        import capo_imagebuilder.types.security_group_ids

        out["securityGroupIds"] = (
            capo_imagebuilder.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "logging" in value:
        import capo_imagebuilder.types.logging

        out["logging"] = capo_imagebuilder.types.logging.serialize_json(
            value["logging"]
        )
    if "key_pair" in value:
        out["keyPair"] = value["key_pair"]
    if "terminate_instance_on_failure" in value:
        out["terminateInstanceOnFailure"] = value["terminate_instance_on_failure"]
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["dateUpdated"] = value["date_updated"]
    if "resource_tags" in value:
        import capo_imagebuilder.types.resource_tag_map

        out["resourceTags"] = capo_imagebuilder.types.resource_tag_map.serialize_json(
            value["resource_tags"]
        )
    if "instance_metadata_options" in value:
        import capo_imagebuilder.types.instance_metadata_options

        out["instanceMetadataOptions"] = (
            capo_imagebuilder.types.instance_metadata_options.serialize_json(
                value["instance_metadata_options"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "placement" in value:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.serialize_json(
            value["placement"]
        )
    return out


def deserialize_json(data: dict) -> InfrastructureConfiguration:
    out: InfrastructureConfiguration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "instanceTypes" in data:
        import capo_imagebuilder.types.instance_type_list

        out["instance_types"] = (
            capo_imagebuilder.types.instance_type_list.deserialize_json(
                data["instanceTypes"]
            )
        )
    if "instanceProfileName" in data:
        out["instance_profile_name"] = data["instanceProfileName"]
    if "securityGroupIds" in data:
        import capo_imagebuilder.types.security_group_ids

        out["security_group_ids"] = (
            capo_imagebuilder.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    if "logging" in data:
        import capo_imagebuilder.types.logging

        out["logging"] = capo_imagebuilder.types.logging.deserialize_json(
            data["logging"]
        )
    if "keyPair" in data:
        out["key_pair"] = data["keyPair"]
    if "terminateInstanceOnFailure" in data:
        out["terminate_instance_on_failure"] = data["terminateInstanceOnFailure"]
    if "snsTopicArn" in data:
        out["sns_topic_arn"] = data["snsTopicArn"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "dateUpdated" in data:
        out["date_updated"] = data["dateUpdated"]
    if "resourceTags" in data:
        import capo_imagebuilder.types.resource_tag_map

        out["resource_tags"] = (
            capo_imagebuilder.types.resource_tag_map.deserialize_json(
                data["resourceTags"]
            )
        )
    if "instanceMetadataOptions" in data:
        import capo_imagebuilder.types.instance_metadata_options

        out["instance_metadata_options"] = (
            capo_imagebuilder.types.instance_metadata_options.deserialize_json(
                data["instanceMetadataOptions"]
            )
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "placement" in data:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.deserialize_json(
            data["placement"]
        )
    return out
