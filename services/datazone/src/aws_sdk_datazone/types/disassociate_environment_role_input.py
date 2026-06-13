"""Generated from Smithy shape ``com.amazonaws.datazone#DisassociateEnvironmentRoleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class DisassociateEnvironmentRoleInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which an environment role is disassociated.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment.</p>"""
    environment_role_arn: "str"
    """<p>The ARN of the environment role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateEnvironmentRoleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateEnvironmentRoleInput:
    out: DisassociateEnvironmentRoleInput = {}  # type: ignore[typeddict-item]
    return out
