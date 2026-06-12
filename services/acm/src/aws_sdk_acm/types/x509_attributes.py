"""Generated from Smithy shape ``com.amazonaws.acm#X509Attributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.distinguished_name
    import aws_sdk_acm.types.extended_key_usage_names
    import aws_sdk_acm.types.general_name_list
    import aws_sdk_acm.types.key_algorithm
    import aws_sdk_acm.types.key_usage_names
    import aws_sdk_acm.types.serial_number
    import aws_sdk_acm.types.t_stamp


class X509Attributes(TypedDict):
    issuer: NotRequired["aws_sdk_acm.types.distinguished_name.DistinguishedName"]
    """<p>The distinguished name of the certificate issuer.</p>"""
    subject: NotRequired["aws_sdk_acm.types.distinguished_name.DistinguishedName"]
    """<p>The distinguished name of the certificate subject.</p>"""
    subject_alternative_names: NotRequired[
        "aws_sdk_acm.types.general_name_list.GeneralNameList"
    ]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p>"""
    extended_key_usages: NotRequired[
        "aws_sdk_acm.types.extended_key_usage_names.ExtendedKeyUsageNames"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    key_algorithm: NotRequired["aws_sdk_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    key_usages: NotRequired["aws_sdk_acm.types.key_usage_names.KeyUsageNames"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    serial_number: NotRequired["aws_sdk_acm.types.serial_number.SerialNumber"]
    """<p>The serial number assigned by the certificate authority.</p>"""
    not_after: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    not_before: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: X509Attributes) -> dict:
    out: dict = {}
    if "issuer" in value:
        import aws_sdk_acm.types.distinguished_name

        out["Issuer"] = aws_sdk_acm.types.distinguished_name.serialize_aws_json_1_1(
            value["issuer"]
        )
    if "subject" in value:
        import aws_sdk_acm.types.distinguished_name

        out["Subject"] = aws_sdk_acm.types.distinguished_name.serialize_aws_json_1_1(
            value["subject"]
        )
    if "subject_alternative_names" in value:
        import aws_sdk_acm.types.general_name_list

        out["SubjectAlternativeNames"] = (
            aws_sdk_acm.types.general_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "extended_key_usages" in value:
        import aws_sdk_acm.types.extended_key_usage_names

        out["ExtendedKeyUsages"] = (
            aws_sdk_acm.types.extended_key_usage_names.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "key_algorithm" in value:
        import aws_sdk_acm.types.key_algorithm

        out["KeyAlgorithm"] = aws_sdk_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "key_usages" in value:
        import aws_sdk_acm.types.key_usage_names

        out["KeyUsages"] = aws_sdk_acm.types.key_usage_names.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "not_after" in value:
        import aws_sdk_acm.types.t_stamp

        out["NotAfter"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "not_before" in value:
        import aws_sdk_acm.types.t_stamp

        out["NotBefore"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> X509Attributes:
    out: X509Attributes = {}  # type: ignore[typeddict-item]
    if "Issuer" in data:
        import aws_sdk_acm.types.distinguished_name

        out["issuer"] = aws_sdk_acm.types.distinguished_name.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    if "Subject" in data:
        import aws_sdk_acm.types.distinguished_name

        out["subject"] = aws_sdk_acm.types.distinguished_name.deserialize_aws_json_1_1(
            data["Subject"]
        )
    if "SubjectAlternativeNames" in data:
        import aws_sdk_acm.types.general_name_list

        out["subject_alternative_names"] = (
            aws_sdk_acm.types.general_name_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if "ExtendedKeyUsages" in data:
        import aws_sdk_acm.types.extended_key_usage_names

        out["extended_key_usages"] = (
            aws_sdk_acm.types.extended_key_usage_names.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if "KeyAlgorithm" in data:
        import aws_sdk_acm.types.key_algorithm

        out["key_algorithm"] = aws_sdk_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if "KeyUsages" in data:
        import aws_sdk_acm.types.key_usage_names

        out["key_usages"] = aws_sdk_acm.types.key_usage_names.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "NotAfter" in data:
        import aws_sdk_acm.types.t_stamp

        out["not_after"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if "NotBefore" in data:
        import aws_sdk_acm.types.t_stamp

        out["not_before"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    return out
