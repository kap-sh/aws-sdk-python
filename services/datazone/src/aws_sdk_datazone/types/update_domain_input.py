"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDomainInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.role_arn
    import aws_sdk_datazone.types.single_sign_on


class UpdateDomainInput(TypedDict):
    identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon Web Services domain that is to be updated.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    single_sign_on: NotRequired["aws_sdk_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    domain_execution_role: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    service_role: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The service role of the domain.</p>"""
    name: NotRequired["str"]
    """<p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "single_sign_on" in value:
        import aws_sdk_datazone.types.single_sign_on

        out["singleSignOn"] = aws_sdk_datazone.types.single_sign_on.serialize_json(
            value["single_sign_on"]
        )
    if "domain_execution_role" in value:
        out["domainExecutionRole"] = value["domain_execution_role"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDomainInput:
    out: UpdateDomainInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "singleSignOn" in data:
        import aws_sdk_datazone.types.single_sign_on

        out["single_sign_on"] = aws_sdk_datazone.types.single_sign_on.deserialize_json(
            data["singleSignOn"]
        )
    if "domainExecutionRole" in data:
        out["domain_execution_role"] = data["domainExecutionRole"]
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "name" in data:
        out["name"] = data["name"]
    return out
