"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcsMetadataDetails``."""

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError


class AwsEcsMetadataDetails(TypedDict, closed=True):
    details_group: "str"
    """<p>The details group information for a task in a cluster.</p>"""
    task_definition_arn: "str"
    """<p>The task definition ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsMetadataDetails) -> dict:
    out: dict = {}
    out["detailsGroup"] = value["details_group"]
    out["taskDefinitionArn"] = value["task_definition_arn"]
    return out


def deserialize_json(data: dict) -> AwsEcsMetadataDetails:
    out: AwsEcsMetadataDetails = {}  # type: ignore[typeddict-item]
    if "detailsGroup" in data:
        out["details_group"] = data["detailsGroup"]
    else:
        raise DeserializationError("AwsEcsMetadataDetails.details_group required")
    if "taskDefinitionArn" in data:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    else:
        raise DeserializationError("AwsEcsMetadataDetails.task_definition_arn required")
    return out
