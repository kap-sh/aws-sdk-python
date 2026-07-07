"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyCertificateBasedAuthPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.certificate_based_auth_properties
    import aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list
    import aws_sdk_workspaces.types.directory_id


class ModifyCertificateBasedAuthPropertiesRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The resource identifiers, in the form of directory IDs.</p>"""
    certificate_based_auth_properties: NotRequired[
        "aws_sdk_workspaces.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
    ]
    """<p>The properties of the certificate-based authentication.</p>"""
    properties_to_delete: NotRequired[
        "aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list.DeletableCertificateBasedAuthPropertiesList"
    ]
    """<p>The properties of the certificate-based authentication you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyCertificateBasedAuthPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "certificate_based_auth_properties" in value:
        import aws_sdk_workspaces.types.certificate_based_auth_properties

        out["CertificateBasedAuthProperties"] = (
            aws_sdk_workspaces.types.certificate_based_auth_properties.serialize_aws_json_1_1(
                value["certificate_based_auth_properties"]
            )
        )
    if "properties_to_delete" in value:
        import aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list

        out["PropertiesToDelete"] = (
            aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list.serialize_aws_json_1_1(
                value["properties_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyCertificateBasedAuthPropertiesRequest:
    out: ModifyCertificateBasedAuthPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "ModifyCertificateBasedAuthPropertiesRequest.resource_id required"
        )
    if "CertificateBasedAuthProperties" in data:
        import aws_sdk_workspaces.types.certificate_based_auth_properties

        out["certificate_based_auth_properties"] = (
            aws_sdk_workspaces.types.certificate_based_auth_properties.deserialize_aws_json_1_1(
                data["CertificateBasedAuthProperties"]
            )
        )
    if "PropertiesToDelete" in data:
        import aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list

        out["properties_to_delete"] = (
            aws_sdk_workspaces.types.deletable_certificate_based_auth_properties_list.deserialize_aws_json_1_1(
                data["PropertiesToDelete"]
            )
        )
    return out
