"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateLakehouseConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace_name


class UpdateLakehouseConfigurationResponse(TypedDict, closed=True):
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace.</p>"""
    lakehouse_idc_application_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation.</p>"""
    lakehouse_registration_status: NotRequired["str"]
    """<p>The current status of the lakehouse registration. Indicates whether the namespace is successfully registered with Amazon Redshift federated permissions.</p>"""
    catalog_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Glue Data Catalog associated with the lakehouse configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLakehouseConfigurationResponse) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "lakehouse_idc_application_arn" in value:
        out["lakehouseIdcApplicationArn"] = value["lakehouse_idc_application_arn"]
    if "lakehouse_registration_status" in value:
        out["lakehouseRegistrationStatus"] = value["lakehouse_registration_status"]
    if "catalog_arn" in value:
        out["catalogArn"] = value["catalog_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLakehouseConfigurationResponse:
    out: UpdateLakehouseConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "lakehouseIdcApplicationArn" in data:
        out["lakehouse_idc_application_arn"] = data["lakehouseIdcApplicationArn"]
    if "lakehouseRegistrationStatus" in data:
        out["lakehouse_registration_status"] = data["lakehouseRegistrationStatus"]
    if "catalogArn" in data:
        out["catalog_arn"] = data["catalogArn"]
    return out
