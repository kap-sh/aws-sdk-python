"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTlsCertificateAuthority``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceConnectTlsCertificateAuthority(TypedDict):
    aws_pca_authority_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the Amazon Web Services Private Certificate Authority certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTlsCertificateAuthority) -> dict:
    out: dict = {}
    if "aws_pca_authority_arn" in value:
        out["awsPcaAuthorityArn"] = value["aws_pca_authority_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTlsCertificateAuthority:
    out: ServiceConnectTlsCertificateAuthority = {}  # type: ignore[typeddict-item]
    if "awsPcaAuthorityArn" in data:
        out["aws_pca_authority_arn"] = data["awsPcaAuthorityArn"]
    return out
