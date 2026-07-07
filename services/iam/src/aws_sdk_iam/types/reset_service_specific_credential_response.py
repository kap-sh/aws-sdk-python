"""Generated from Smithy shape ``com.amazonaws.iam#ResetServiceSpecificCredentialResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.service_specific_credential


class ResetServiceSpecificCredentialResponse(TypedDict, closed=True):
    service_specific_credential: NotRequired[
        "aws_sdk_iam.types.service_specific_credential.ServiceSpecificCredential"
    ]
    """<p>A structure with details about the updated service-specific credential, including the new password.</p> <important> <p>This is the <b>only</b> time that you can access the password. You cannot recover the password later, but you can reset it again.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetServiceSpecificCredentialResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_specific_credential" in value:
        import aws_sdk_iam.types.service_specific_credential

        aws_sdk_iam.types.service_specific_credential.serialize_query(
            value["service_specific_credential"],
            pairs,
            f"{prefix}.ServiceSpecificCredential",
        )


def deserialize_query(el: Element) -> ResetServiceSpecificCredentialResponse:
    out: ResetServiceSpecificCredentialResponse = {}  # type: ignore[typeddict-item]
    child_service_specific_credential = el.find("ServiceSpecificCredential")
    if child_service_specific_credential is not None:
        import aws_sdk_iam.types.service_specific_credential

        out["service_specific_credential"] = (
            aws_sdk_iam.types.service_specific_credential.deserialize_query(
                child_service_specific_credential
            )
        )
    return out
