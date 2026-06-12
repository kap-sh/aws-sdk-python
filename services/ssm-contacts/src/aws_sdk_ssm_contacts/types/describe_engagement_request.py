"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DescribeEngagementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class DescribeEngagementRequest(TypedDict):
    engagement_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement you want the details of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngagementRequest) -> dict:
    out: dict = {}
    out["EngagementId"] = value["engagement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngagementRequest:
    out: DescribeEngagementRequest = {}  # type: ignore[typeddict-item]
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    else:
        raise DeserializationError("DescribeEngagementRequest.engagement_id required")
    return out
