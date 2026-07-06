"""Generated from Smithy shape ``com.amazonaws.redshift#HsmClientCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class HsmClientCertificate(TypedDict, closed=True):
    hsm_client_certificate_identifier: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The identifier of the HSM client certificate.</p>"""
    hsm_client_certificate_public_key: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The public key that the Amazon Redshift cluster will use to connect to the HSM. You must register the public key in the HSM.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the HSM client certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmClientCertificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_client_certificate_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmClientCertificateIdentifier",
                str(value["hsm_client_certificate_identifier"]),
            )
        )
    if "hsm_client_certificate_public_key" in value:
        pairs.append(
            (
                f"{prefix}.HsmClientCertificatePublicKey",
                str(value["hsm_client_certificate_public_key"]),
            )
        )
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> HsmClientCertificate:
    out: HsmClientCertificate = {}  # type: ignore[typeddict-item]
    child_hsm_client_certificate_identifier = el.find("HsmClientCertificateIdentifier")
    if child_hsm_client_certificate_identifier is not None:
        out["hsm_client_certificate_identifier"] = str(
            child_hsm_client_certificate_identifier.text or ""
        )
    child_hsm_client_certificate_public_key = el.find("HsmClientCertificatePublicKey")
    if child_hsm_client_certificate_public_key is not None:
        out["hsm_client_certificate_public_key"] = str(
            child_hsm_client_certificate_public_key.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    return out
