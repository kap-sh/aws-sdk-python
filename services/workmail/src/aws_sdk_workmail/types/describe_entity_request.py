"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.organization_id


class DescribeEntityRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the entity exists.</p>"""
    email: "aws_sdk_workmail.types.email_address.EmailAddress"
    """<p>The email under which the entity exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityRequest:
    out: DescribeEntityRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DescribeEntityRequest.organization_id required")
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("DescribeEntityRequest.email required")
    return out
