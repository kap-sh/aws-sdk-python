"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_resource_type
    import aws_sdk_guardduty.types.resource_data
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags


class ResourceV2(TypedDict):
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique identifier of the resource.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the resource.</p>"""
    account_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID to which the resource belongs.</p>"""
    resource_type: NotRequired[
        "aws_sdk_guardduty.types.finding_resource_type.FindingResourceType"
    ]
    """<p>The type of the Amazon Web Services resource.</p>"""
    region: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services Region where the resource belongs.</p>"""
    service: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services service of the resource.</p>"""
    cloud_partition: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The cloud partition within the Amazon Web Services Region to which the resource belongs.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>Contains information about the tags associated with the resource.</p>"""
    data: NotRequired["aws_sdk_guardduty.types.resource_data.ResourceData"]
    """<p>Contains information about the Amazon Web Services resource associated with the activity that prompted GuardDuty to generate a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceV2) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["name"] = value["name"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "resource_type" in value:
        import aws_sdk_guardduty.types.finding_resource_type

        out["resourceType"] = (
            aws_sdk_guardduty.types.finding_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "service" in value:
        out["service"] = value["service"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    if "data" in value:
        import aws_sdk_guardduty.types.resource_data

        out["data"] = aws_sdk_guardduty.types.resource_data.serialize_json(
            value["data"]
        )
    return out


def deserialize_json(data: dict) -> ResourceV2:
    out: ResourceV2 = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "name" in data:
        out["name"] = data["name"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "resourceType" in data:
        import aws_sdk_guardduty.types.finding_resource_type

        out["resource_type"] = (
            aws_sdk_guardduty.types.finding_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "service" in data:
        out["service"] = data["service"]
    if "cloudPartition" in data:
        out["cloud_partition"] = data["cloudPartition"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    if "data" in data:
        import aws_sdk_guardduty.types.resource_data

        out["data"] = aws_sdk_guardduty.types.resource_data.deserialize_json(
            data["data"]
        )
    return out
