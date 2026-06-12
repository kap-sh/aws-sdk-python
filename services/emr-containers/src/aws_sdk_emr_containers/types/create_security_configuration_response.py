"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateSecurityConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.security_configuration_arn


class CreateSecurityConfigurationResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the security configuration.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the security configuration.</p>"""
    arn: NotRequired[
        "aws_sdk_emr_containers.types.security_configuration_arn.SecurityConfigurationArn"
    ]
    """<p>The ARN (Amazon Resource Name) of the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityConfigurationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateSecurityConfigurationResponse:
    out: CreateSecurityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
