"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCustomDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.custom_domain_name
    import aws_sdk_redshift_serverless.types.workgroup_name


class GetCustomDomainAssociationRequest(TypedDict, closed=True):
    custom_domain_name: (
        "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName"
    )
    """<p>The custom domain name associated with the workgroup.</p>"""
    workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCustomDomainAssociationRequest) -> dict:
    out: dict = {}
    out["customDomainName"] = value["custom_domain_name"]
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCustomDomainAssociationRequest:
    out: GetCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    else:
        raise DeserializationError(
            "GetCustomDomainAssociationRequest.custom_domain_name required"
        )
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError(
            "GetCustomDomainAssociationRequest.workgroup_name required"
        )
    return out
