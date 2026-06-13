"""Generated from Smithy shape ``com.amazonaws.datazone#AssociateEnvironmentRoleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class AssociateEnvironmentRoleInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment role is associated.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the Amazon DataZone environment.</p>"""
    environment_role_arn: "str"
    """<p>The ARN of the environment role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEnvironmentRoleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateEnvironmentRoleInput:
    out: AssociateEnvironmentRoleInput = {}  # type: ignore[typeddict-item]
    return out
