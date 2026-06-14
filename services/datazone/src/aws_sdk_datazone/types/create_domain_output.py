"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDomainOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_status
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.domain_version
    import aws_sdk_datazone.types.kms_key_arn
    import aws_sdk_datazone.types.role_arn
    import aws_sdk_datazone.types.single_sign_on
    import aws_sdk_datazone.types.tags


class CreateDomainOutput(TypedDict):
    id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    root_domain_unit_id: NotRequired[
        "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>The ID of the root domain unit.</p>"""
    name: NotRequired["str"]
    """<p>The name of the Amazon DataZone domain.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon DataZone domain.</p>"""
    single_sign_on: NotRequired["aws_sdk_datazone.types.single_sign_on.SingleSignOn"]
    """<p>The single-sign on configuration of the Amazon DataZone domain.</p>"""
    domain_execution_role: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN of the Amazon DataZone domain.</p>"""
    kms_key_identifier: NotRequired["aws_sdk_datazone.types.kms_key_arn.KmsKeyArn"]
    """<p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>"""
    status: NotRequired["aws_sdk_datazone.types.domain_status.DomainStatus"]
    """<p>The status of the Amazon DataZone domain.</p>"""
    portal_url: NotRequired["str"]
    """<p>The URL of the data portal for this Amazon DataZone domain.</p>"""
    tags: NotRequired["aws_sdk_datazone.types.tags.Tags"]
    """<p>The tags specified for the Amazon DataZone domain.</p>"""
    domain_version: NotRequired["aws_sdk_datazone.types.domain_version.DomainVersion"]
    """<p>The version of the domain that is created.</p>"""
    service_role: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>Te service role of the domain that is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "root_domain_unit_id" in value:
        out["rootDomainUnitId"] = value["root_domain_unit_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "single_sign_on" in value:
        import aws_sdk_datazone.types.single_sign_on

        out["singleSignOn"] = aws_sdk_datazone.types.single_sign_on.serialize_json(
            value["single_sign_on"]
        )
    if "domain_execution_role" in value:
        out["domainExecutionRole"] = value["domain_execution_role"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "status" in value:
        import aws_sdk_datazone.types.domain_status

        out["status"] = aws_sdk_datazone.types.domain_status.serialize_json(
            value["status"]
        )
    if "portal_url" in value:
        out["portalUrl"] = value["portal_url"]
    if "tags" in value:
        import aws_sdk_datazone.types.tags

        out["tags"] = aws_sdk_datazone.types.tags.serialize_json(value["tags"])
    if "domain_version" in value:
        import aws_sdk_datazone.types.domain_version

        out["domainVersion"] = aws_sdk_datazone.types.domain_version.serialize_json(
            value["domain_version"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    return out


def deserialize_json(data: dict) -> CreateDomainOutput:
    out: CreateDomainOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDomainOutput.id required")
    if "rootDomainUnitId" in data:
        out["root_domain_unit_id"] = data["rootDomainUnitId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "singleSignOn" in data:
        import aws_sdk_datazone.types.single_sign_on

        out["single_sign_on"] = aws_sdk_datazone.types.single_sign_on.deserialize_json(
            data["singleSignOn"]
        )
    if "domainExecutionRole" in data:
        out["domain_execution_role"] = data["domainExecutionRole"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if "status" in data:
        import aws_sdk_datazone.types.domain_status

        out["status"] = aws_sdk_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    if "portalUrl" in data:
        out["portal_url"] = data["portalUrl"]
    if "tags" in data:
        import aws_sdk_datazone.types.tags

        out["tags"] = aws_sdk_datazone.types.tags.deserialize_json(data["tags"])
    if "domainVersion" in data:
        import aws_sdk_datazone.types.domain_version

        out["domain_version"] = aws_sdk_datazone.types.domain_version.deserialize_json(
            data["domainVersion"]
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    return out
