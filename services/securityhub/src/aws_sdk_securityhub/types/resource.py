"""Generated from Smithy shape ``com.amazonaws.securityhub#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.data_classification_details
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.partition
    import aws_sdk_securityhub.types.resource_details


class Resource(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the resource that details are provided for. If possible, set <code>Type</code> to one of the supported resource types. For example, if the resource is an EC2 instance, then set <code>Type</code> to <code>AwsEc2Instance</code>.</p> <p>If the resource does not match any of the provided types, then set <code>Type</code> to <code>Other</code>. </p> <p>Length Constraints: Minimum length of 1. Maximum length of 256.</p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical identifier for the given resource type.</p>"""
    partition: NotRequired["aws_sdk_securityhub.types.partition.Partition"]
    """<p>The canonical Amazon Web Services partition name that the Region is assigned to.</p>"""
    region: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical Amazon Web Services external Region name where this resource is located.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 16.</p>"""
    resource_role: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Identifies the role of the resource in the finding. A resource is either the actor or target of the finding activity,</p>"""
    tags: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    r"""<p>A list of Amazon Web Services tags associated with a resource at the time the finding was processed. Tags must follow <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions\">Amazon Web Services tag naming limits and requirements</a>.</p>"""
    data_classification: NotRequired[
        "aws_sdk_securityhub.types.data_classification_details.DataClassificationDetails"
    ]
    """<p>Contains information about sensitive data that was detected on the resource.</p>"""
    details: NotRequired["aws_sdk_securityhub.types.resource_details.ResourceDetails"]
    """<p>Additional details about the resource related to a finding.</p>"""
    application_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the application that is related to a finding. </p>"""
    application_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the application that is related to a finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "partition" in value:
        import aws_sdk_securityhub.types.partition

        out["Partition"] = aws_sdk_securityhub.types.partition.serialize_json(
            value["partition"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_role" in value:
        out["ResourceRole"] = value["resource_role"]
    if "tags" in value:
        import aws_sdk_securityhub.types.field_map

        out["Tags"] = aws_sdk_securityhub.types.field_map.serialize_json(value["tags"])
    if "data_classification" in value:
        import aws_sdk_securityhub.types.data_classification_details

        out["DataClassification"] = (
            aws_sdk_securityhub.types.data_classification_details.serialize_json(
                value["data_classification"]
            )
        )
    if "details" in value:
        import aws_sdk_securityhub.types.resource_details

        out["Details"] = aws_sdk_securityhub.types.resource_details.serialize_json(
            value["details"]
        )
    if "application_name" in value:
        out["ApplicationName"] = value["application_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Partition" in data:
        import aws_sdk_securityhub.types.partition

        out["partition"] = aws_sdk_securityhub.types.partition.deserialize_json(
            data["Partition"]
        )
    if "Region" in data:
        out["region"] = data["Region"]
    if "ResourceRole" in data:
        out["resource_role"] = data["ResourceRole"]
    if "Tags" in data:
        import aws_sdk_securityhub.types.field_map

        out["tags"] = aws_sdk_securityhub.types.field_map.deserialize_json(data["Tags"])
    if "DataClassification" in data:
        import aws_sdk_securityhub.types.data_classification_details

        out["data_classification"] = (
            aws_sdk_securityhub.types.data_classification_details.deserialize_json(
                data["DataClassification"]
            )
        )
    if "Details" in data:
        import aws_sdk_securityhub.types.resource_details

        out["details"] = aws_sdk_securityhub.types.resource_details.deserialize_json(
            data["Details"]
        )
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
