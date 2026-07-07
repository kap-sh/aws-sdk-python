"""Generated from Smithy shape ``com.amazonaws.acm#ImportCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn
    import aws_sdk_acm.types.certificate_body_blob
    import aws_sdk_acm.types.certificate_chain_blob
    import aws_sdk_acm.types.private_key_blob
    import aws_sdk_acm.types.tag_list


class ImportCertificateRequest(TypedDict, closed=True):
    certificate_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of an imported certificate to replace. To import a new certificate, omit this field. </p>"""
    certificate: "aws_sdk_acm.types.certificate_body_blob.CertificateBodyBlob"
    """<p>The certificate to import.</p>"""
    private_key: "aws_sdk_acm.types.private_key_blob.PrivateKeyBlob"
    """<p>The private key that matches the public key in the certificate.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_acm.types.certificate_chain_blob.CertificateChainBlob"
    ]
    """<p>The PEM encoded certificate chain.</p>"""
    tags: NotRequired["aws_sdk_acm.types.tag_list.TagList"]
    """<p>One or more resource tags to associate with the imported certificate. </p> <p>Note: You cannot apply tags when reimporting a certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateRequest) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    import aws_sdk_acm.types.certificate_body_blob

    out["Certificate"] = aws_sdk_acm.types.certificate_body_blob.serialize_aws_json_1_1(
        value["certificate"]
    )
    import aws_sdk_acm.types.private_key_blob

    out["PrivateKey"] = aws_sdk_acm.types.private_key_blob.serialize_aws_json_1_1(
        value["private_key"]
    )
    if "certificate_chain" in value:
        import aws_sdk_acm.types.certificate_chain_blob

        out["CertificateChain"] = (
            aws_sdk_acm.types.certificate_chain_blob.serialize_aws_json_1_1(
                value["certificate_chain"]
            )
        )
    if "tags" in value:
        import aws_sdk_acm.types.tag_list

        out["Tags"] = aws_sdk_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateRequest:
    out: ImportCertificateRequest = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "Certificate" in data:
        import aws_sdk_acm.types.certificate_body_blob

        out["certificate"] = (
            aws_sdk_acm.types.certificate_body_blob.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    else:
        raise DeserializationError("ImportCertificateRequest.certificate required")
    if "PrivateKey" in data:
        import aws_sdk_acm.types.private_key_blob

        out["private_key"] = (
            aws_sdk_acm.types.private_key_blob.deserialize_aws_json_1_1(
                data["PrivateKey"]
            )
        )
    else:
        raise DeserializationError("ImportCertificateRequest.private_key required")
    if "CertificateChain" in data:
        import aws_sdk_acm.types.certificate_chain_blob

        out["certificate_chain"] = (
            aws_sdk_acm.types.certificate_chain_blob.deserialize_aws_json_1_1(
                data["CertificateChain"]
            )
        )
    if "Tags" in data:
        import aws_sdk_acm.types.tag_list

        out["tags"] = aws_sdk_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
