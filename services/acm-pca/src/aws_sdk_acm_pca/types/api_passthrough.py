"""Generated from Smithy shape ``com.amazonaws.acmpca#ApiPassthrough``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.asn1_subject
    import aws_sdk_acm_pca.types.extensions


class ApiPassthrough(TypedDict):
    extensions: NotRequired["aws_sdk_acm_pca.types.extensions.Extensions"]
    """<p>Specifies X.509 extension information for a certificate.</p>"""
    subject: NotRequired["aws_sdk_acm_pca.types.asn1_subject.ASN1Subject"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiPassthrough) -> dict:
    out: dict = {}
    if "extensions" in value:
        import aws_sdk_acm_pca.types.extensions

        out["Extensions"] = aws_sdk_acm_pca.types.extensions.serialize_aws_json_1_1(
            value["extensions"]
        )
    if "subject" in value:
        import aws_sdk_acm_pca.types.asn1_subject

        out["Subject"] = aws_sdk_acm_pca.types.asn1_subject.serialize_aws_json_1_1(
            value["subject"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApiPassthrough:
    out: ApiPassthrough = {}  # type: ignore[typeddict-item]
    if "Extensions" in data:
        import aws_sdk_acm_pca.types.extensions

        out["extensions"] = aws_sdk_acm_pca.types.extensions.deserialize_aws_json_1_1(
            data["Extensions"]
        )
    if "Subject" in data:
        import aws_sdk_acm_pca.types.asn1_subject

        out["subject"] = aws_sdk_acm_pca.types.asn1_subject.deserialize_aws_json_1_1(
            data["Subject"]
        )
    return out
