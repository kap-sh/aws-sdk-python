"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiAggregationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.ami_id
    import aws_sdk_inspector2.types.severity_counts


class AmiAggregationResponse(TypedDict):
    ami: "aws_sdk_inspector2.types.ami_id.AmiId"
    """<p>The ID of the AMI that findings were aggregated for.</p>"""
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the AMI.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>An object that contains the count of matched findings per severity.</p>"""
    affected_instances: NotRequired["int"]
    """<p>The IDs of Amazon EC2 instances using this AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiAggregationResponse) -> dict:
    out: dict = {}
    out["ami"] = value["ami"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "affected_instances" in value:
        out["affectedInstances"] = value["affected_instances"]
    return out


def deserialize_json(data: dict) -> AmiAggregationResponse:
    out: AmiAggregationResponse = {}  # type: ignore[typeddict-item]
    if "ami" in data:
        out["ami"] = data["ami"]
    else:
        raise DeserializationError("AmiAggregationResponse.ami required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    if "affectedInstances" in data:
        out["affected_instances"] = data["affectedInstances"]
    return out
