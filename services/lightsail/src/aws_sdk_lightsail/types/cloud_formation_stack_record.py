"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list
    import aws_sdk_lightsail.types.destination_info
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.record_state
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type


class CloudFormationStackRecord(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the CloudFormation stack record. It starts with <code>CloudFormationStackRecord</code> followed by a GUID.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the CloudFormation stack record.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the CloudFormation stack record was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>A list of objects describing the Availability Zone and Amazon Web Services Region of the CloudFormation stack record.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>CloudFormationStackRecord</code>).</p>"""
    state: NotRequired["aws_sdk_lightsail.types.record_state.RecordState"]
    """<p>The current state of the CloudFormation stack record.</p>"""
    source_info: NotRequired[
        "aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list.CloudFormationStackRecordSourceInfoList"
    ]
    """<p>A list of objects describing the source of the CloudFormation stack record.</p>"""
    destination_info: NotRequired[
        "aws_sdk_lightsail.types.destination_info.DestinationInfo"
    ]
    """<p>A list of objects describing the destination service, which is AWS CloudFormation, and the Amazon Resource Name (ARN) of the AWS CloudFormation stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationStackRecord) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "state" in value:
        import aws_sdk_lightsail.types.record_state

        out["state"] = aws_sdk_lightsail.types.record_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "source_info" in value:
        import aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list

        out["sourceInfo"] = (
            aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list.serialize_aws_json_1_1(
                value["source_info"]
            )
        )
    if "destination_info" in value:
        import aws_sdk_lightsail.types.destination_info

        out["destinationInfo"] = (
            aws_sdk_lightsail.types.destination_info.serialize_aws_json_1_1(
                value["destination_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudFormationStackRecord:
    out: CloudFormationStackRecord = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "state" in data:
        import aws_sdk_lightsail.types.record_state

        out["state"] = aws_sdk_lightsail.types.record_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if "sourceInfo" in data:
        import aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list

        out["source_info"] = (
            aws_sdk_lightsail.types.cloud_formation_stack_record_source_info_list.deserialize_aws_json_1_1(
                data["sourceInfo"]
            )
        )
    if "destinationInfo" in data:
        import aws_sdk_lightsail.types.destination_info

        out["destination_info"] = (
            aws_sdk_lightsail.types.destination_info.deserialize_aws_json_1_1(
                data["destinationInfo"]
            )
        )
    return out
