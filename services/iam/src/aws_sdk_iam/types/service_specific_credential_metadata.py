"""Generated from Smithy shape ``com.amazonaws.iam#ServiceSpecificCredentialMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.service_credential_alias
    import aws_sdk_iam.types.service_name
    import aws_sdk_iam.types.service_specific_credential_id
    import aws_sdk_iam.types.service_user_name
    import aws_sdk_iam.types.status_type
    import aws_sdk_iam.types.user_name_type


class ServiceSpecificCredentialMetadata(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The name of the IAM user associated with the service-specific credential.</p>"""
    status: "aws_sdk_iam.types.status_type.statusType"
    """<p>The status of the service-specific credential. <code>Active</code> means that the key is valid for API calls, while <code>Inactive</code> means it is not.</p>"""
    service_user_name: "aws_sdk_iam.types.service_user_name.serviceUserName"
    """<p>The generated user name for the service-specific credential.</p>"""
    service_credential_alias: NotRequired[
        "aws_sdk_iam.types.service_credential_alias.serviceCredentialAlias"
    ]
    """<p>For Bedrock API keys and CloudWatch Logs API keys, this is the public portion of the credential that includes the IAM user name and a suffix containing version and creation information.</p>"""
    create_date: "aws_sdk_iam.types.date_type.dateType"
    """<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the service-specific credential were created.</p>"""
    expiration_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date and time when the service specific credential expires. This field is only present for Bedrock API keys and CloudWatch Logs API keys that were created with an expiration period.</p>"""
    service_specific_credential_id: (
        "aws_sdk_iam.types.service_specific_credential_id.serviceSpecificCredentialId"
    )
    """<p>The unique identifier for the service-specific credential.</p>"""
    service_name: "aws_sdk_iam.types.service_name.serviceName"
    """<p>The name of the service associated with the service-specific credential.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceSpecificCredentialMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    import aws_sdk_iam.types.status_type

    aws_sdk_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )
    pairs.append((f"{prefix}.ServiceUserName", str(value.get("service_user_name", ""))))
    if "service_credential_alias" in value:
        pairs.append(
            (f"{prefix}.ServiceCredentialAlias", str(value["service_credential_alias"]))
        )
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["create_date"], pairs, f"{prefix}.CreateDate"
    )
    if "expiration_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["expiration_date"], pairs, f"{prefix}.ExpirationDate"
        )
    pairs.append(
        (
            f"{prefix}.ServiceSpecificCredentialId",
            str(value["service_specific_credential_id"]),
        )
    )
    pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))


def deserialize_query(el: Element) -> ServiceSpecificCredentialMetadata:
    out: ServiceSpecificCredentialMetadata = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError(
            "ServiceSpecificCredentialMetadata.user_name required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_iam.types.status_type

        out["status"] = aws_sdk_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("ServiceSpecificCredentialMetadata.status required")
    child_service_user_name = el.find("ServiceUserName")
    if child_service_user_name is not None:
        out["service_user_name"] = str(child_service_user_name.text or "")
    else:
        out["service_user_name"] = ""
    child_service_credential_alias = el.find("ServiceCredentialAlias")
    if child_service_credential_alias is not None:
        out["service_credential_alias"] = str(child_service_credential_alias.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    else:
        raise DeserializationError(
            "ServiceSpecificCredentialMetadata.create_date required"
        )
    child_expiration_date = el.find("ExpirationDate")
    if child_expiration_date is not None:
        import aws_sdk_iam.types.date_type

        out["expiration_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_expiration_date
        )
    child_service_specific_credential_id = el.find("ServiceSpecificCredentialId")
    if child_service_specific_credential_id is not None:
        out["service_specific_credential_id"] = str(
            child_service_specific_credential_id.text or ""
        )
    else:
        raise DeserializationError(
            "ServiceSpecificCredentialMetadata.service_specific_credential_id required"
        )
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    else:
        raise DeserializationError(
            "ServiceSpecificCredentialMetadata.service_name required"
        )
    return out
