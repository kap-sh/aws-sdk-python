"""Generated from Smithy shape ``com.amazonaws.iam#CreateServiceSpecificCredentialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.credential_age_days
    import aws_sdk_iam.types.service_name
    import aws_sdk_iam.types.user_name_type


class CreateServiceSpecificCredentialRequest(TypedDict, closed=True):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    r"""<p>The name of the IAM user that is to be associated with the credentials. The new service-specific credentials have the same permissions as the associated user except that they can be used only to access the specified service.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    service_name: "aws_sdk_iam.types.service_name.serviceName"
    """<p>The name of the Amazon Web Services service that is to be associated with the credentials. The service you specify here is the only service that can be accessed using these credentials.</p>"""
    credential_age_days: NotRequired[
        "aws_sdk_iam.types.credential_age_days.credentialAgeDays"
    ]
    """<p>The number of days until the service specific credential expires. This field is only valid for Bedrock and CloudWatch Logs API keys and must be a positive integer. When not specified, the credential will not expire.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServiceSpecificCredentialRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))
    if "credential_age_days" in value:
        pairs.append((f"{prefix}.CredentialAgeDays", str(value["credential_age_days"])))


def deserialize_query(el: Element) -> CreateServiceSpecificCredentialRequest:
    out: CreateServiceSpecificCredentialRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError(
            "CreateServiceSpecificCredentialRequest.user_name required"
        )
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    else:
        raise DeserializationError(
            "CreateServiceSpecificCredentialRequest.service_name required"
        )
    child_credential_age_days = el.find("CredentialAgeDays")
    if child_credential_age_days is not None:
        out["credential_age_days"] = int(child_credential_age_days.text or "")
    return out
