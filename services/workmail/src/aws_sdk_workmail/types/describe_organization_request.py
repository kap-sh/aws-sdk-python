"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id


class DescribeOrganizationRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization to be described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationRequest:
    out: DescribeOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DescribeOrganizationRequest.organization_id required"
        )
    return out
