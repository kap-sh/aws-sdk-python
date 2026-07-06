"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StartEngagementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class StartEngagementResult(TypedDict, closed=True):
    engagement_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEngagementResult) -> dict:
    out: dict = {}
    out["EngagementArn"] = value["engagement_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEngagementResult:
    out: StartEngagementResult = {}  # type: ignore[typeddict-item]
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        raise DeserializationError("StartEngagementResult.engagement_arn required")
    return out
