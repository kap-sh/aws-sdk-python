"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceSpecificCredentialRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.service_specific_credential_id
    import aws_sdk_iam.types.user_name_type


class DeleteServiceSpecificCredentialRequest(TypedDict):
    user_name: NotRequired["aws_sdk_iam.types.user_name_type.userNameType"]
    """<p>The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    service_specific_credential_id: (
        "aws_sdk_iam.types.service_specific_credential_id.serviceSpecificCredentialId"
    )
    """<p>The unique identifier of the service-specific credential. You can get this value by calling <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServiceSpecificCredentials.html\">ListServiceSpecificCredentials</a>.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters that can consist of any upper or lowercased letter or digit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServiceSpecificCredentialRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append(
        (
            f"{prefix}.ServiceSpecificCredentialId",
            str(value["service_specific_credential_id"]),
        )
    )


def deserialize_query(el: Element) -> DeleteServiceSpecificCredentialRequest:
    out: DeleteServiceSpecificCredentialRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_service_specific_credential_id = el.find("ServiceSpecificCredentialId")
    if child_service_specific_credential_id is not None:
        out["service_specific_credential_id"] = str(
            child_service_specific_credential_id.text or ""
        )
    else:
        raise DeserializationError(
            "DeleteServiceSpecificCredentialRequest.service_specific_credential_id required"
        )
    return out
