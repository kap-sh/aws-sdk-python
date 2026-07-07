"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeInboundDmarcSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id


class DescribeInboundDmarcSettingsRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>Lists the ID of the given organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInboundDmarcSettingsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInboundDmarcSettingsRequest:
    out: DescribeInboundDmarcSettingsRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DescribeInboundDmarcSettingsRequest.organization_id required"
        )
    return out
