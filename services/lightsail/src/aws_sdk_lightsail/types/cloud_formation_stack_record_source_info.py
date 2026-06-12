"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecordSourceInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.cloud_formation_stack_record_source_type
    import aws_sdk_lightsail.types.non_empty_string


class CloudFormationStackRecordSourceInfo(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_lightsail.types.cloud_formation_stack_record_source_type.CloudFormationStackRecordSourceType"
    ]
    """<p>The Lightsail resource type (<code>ExportSnapshotRecord</code>).</p>"""
    name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the record.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the export snapshot record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationStackRecordSourceInfo) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_lightsail.types.cloud_formation_stack_record_source_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.cloud_formation_stack_record_source_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudFormationStackRecordSourceInfo:
    out: CloudFormationStackRecordSourceInfo = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_lightsail.types.cloud_formation_stack_record_source_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.cloud_formation_stack_record_source_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
