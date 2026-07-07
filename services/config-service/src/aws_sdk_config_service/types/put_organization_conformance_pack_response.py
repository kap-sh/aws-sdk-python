"""Generated from Smithy shape ``com.amazonaws.configservice#PutOrganizationConformancePackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit256


class PutOrganizationConformancePackResponse(TypedDict, closed=True):
    organization_conformance_pack_arn: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>ARN of the organization conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutOrganizationConformancePackResponse) -> dict:
    out: dict = {}
    if "organization_conformance_pack_arn" in value:
        out["OrganizationConformancePackArn"] = value[
            "organization_conformance_pack_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutOrganizationConformancePackResponse:
    out: PutOrganizationConformancePackResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConformancePackArn" in data:
        out["organization_conformance_pack_arn"] = data[
            "OrganizationConformancePackArn"
        ]
    return out
