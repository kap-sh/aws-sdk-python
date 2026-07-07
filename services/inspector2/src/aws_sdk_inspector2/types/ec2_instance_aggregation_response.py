"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2InstanceAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ami_id
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.severity_counts
    import aws_sdk_inspector2.types.tag_map


class Ec2InstanceAggregationResponse(TypedDict, closed=True):
    instance_id: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The Amazon EC2 instance ID.</p>"""
    ami: NotRequired["aws_sdk_inspector2.types.ami_id.AmiId"]
    """<p>The Amazon Machine Image (AMI) of the Amazon EC2 instance.</p>"""
    operating_system: NotRequired["str"]
    """<p>The operating system of the Amazon EC2 instance.</p>"""
    instance_tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags attached to the instance.</p>"""
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account for the Amazon EC2 instance.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>An object that contains the count of matched findings per severity.</p>"""
    network_findings: NotRequired["int"]
    """<p>The number of network findings for the Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2InstanceAggregationResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    if "ami" in value:
        out["ami"] = value["ami"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "instance_tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["instanceTags"] = aws_sdk_inspector2.types.tag_map.serialize_json(
            value["instance_tags"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "network_findings" in value:
        out["networkFindings"] = value["network_findings"]
    return out


def deserialize_json(data: dict) -> Ec2InstanceAggregationResponse:
    out: Ec2InstanceAggregationResponse = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError(
            "Ec2InstanceAggregationResponse.instance_id required"
        )
    if "ami" in data:
        out["ami"] = data["ami"]
    if "operatingSystem" in data:
        out["operating_system"] = data["operatingSystem"]
    if "instanceTags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["instance_tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(
            data["instanceTags"]
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    if "networkFindings" in data:
        out["network_findings"] = data["networkFindings"]
    return out
