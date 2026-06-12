"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteOrganizationConformancePackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_conformance_pack_name


class DeleteOrganizationConformancePackRequest(TypedDict):
    organization_conformance_pack_name: "aws_sdk_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>The name of organization conformance pack that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationConformancePackRequest) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationConformancePackRequest:
    out: DeleteOrganizationConformancePackRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConformancePackName" in data:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        raise DeserializationError(
            "DeleteOrganizationConformancePackRequest.organization_conformance_pack_name required"
        )
    return out
