"""Generated from Smithy shape ``com.amazonaws.workmail#ListMobileDeviceAccessRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.organization_id


class ListMobileDeviceAccessRulesRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which to list the rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileDeviceAccessRulesRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileDeviceAccessRulesRequest:
    out: ListMobileDeviceAccessRulesRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "ListMobileDeviceAccessRulesRequest.organization_id required"
        )
    return out
