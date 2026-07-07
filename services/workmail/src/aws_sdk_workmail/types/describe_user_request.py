"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.organization_id


class DescribeUserRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the user exists.</p>"""
    user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the user to be described.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserRequest:
    out: DescribeUserRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DescribeUserRequest.organization_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DescribeUserRequest.user_id required")
    return out
