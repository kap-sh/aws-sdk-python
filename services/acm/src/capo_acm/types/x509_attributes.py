"""Generated from Smithy shape ``com.amazonaws.acm#X509Attributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.distinguished_name
    import capo_acm.types.extended_key_usage_names
    import capo_acm.types.general_name_list
    import capo_acm.types.key_algorithm
    import capo_acm.types.key_usage_names
    import capo_acm.types.serial_number
    import capo_acm.types.t_stamp


class X509Attributes(TypedDict, closed=True):
    issuer: NotRequired["capo_acm.types.distinguished_name.DistinguishedName"]
    """<p>The distinguished name of the certificate issuer.</p>"""
    subject: NotRequired["capo_acm.types.distinguished_name.DistinguishedName"]
    """<p>The distinguished name of the certificate subject.</p>"""
    subject_alternative_names: NotRequired[
        "capo_acm.types.general_name_list.GeneralNameList"
    ]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p>"""
    extended_key_usages: NotRequired[
        "capo_acm.types.extended_key_usage_names.ExtendedKeyUsageNames"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    key_algorithm: NotRequired["capo_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    key_usages: NotRequired["capo_acm.types.key_usage_names.KeyUsageNames"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    serial_number: NotRequired["capo_acm.types.serial_number.SerialNumber"]
    """<p>The serial number assigned by the certificate authority.</p>"""
    not_after: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    not_before: NotRequired["capo_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: X509Attributes) -> dict:
    out: dict = {}
    if "issuer" in value:
        import capo_acm.types.distinguished_name

        out["Issuer"] = capo_acm.types.distinguished_name.serialize_aws_json_1_1(
            value["issuer"]
        )
    if "subject" in value:
        import capo_acm.types.distinguished_name

        out["Subject"] = capo_acm.types.distinguished_name.serialize_aws_json_1_1(
            value["subject"]
        )
    if "subject_alternative_names" in value:
        import capo_acm.types.general_name_list

        out["SubjectAlternativeNames"] = (
            capo_acm.types.general_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "extended_key_usages" in value:
        import capo_acm.types.extended_key_usage_names

        out["ExtendedKeyUsages"] = (
            capo_acm.types.extended_key_usage_names.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "key_algorithm" in value:
        import capo_acm.types.key_algorithm

        out["KeyAlgorithm"] = capo_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "key_usages" in value:
        import capo_acm.types.key_usage_names

        out["KeyUsages"] = capo_acm.types.key_usage_names.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "not_after" in value:
        import capo_acm.types.t_stamp

        out["NotAfter"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "not_before" in value:
        import capo_acm.types.t_stamp

        out["NotBefore"] = capo_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> X509Attributes:
    out: X509Attributes = {}  # type: ignore[typeddict-item]
    if "Issuer" in data:
        import capo_acm.types.distinguished_name

        out["issuer"] = capo_acm.types.distinguished_name.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    if "Subject" in data:
        import capo_acm.types.distinguished_name

        out["subject"] = capo_acm.types.distinguished_name.deserialize_aws_json_1_1(
            data["Subject"]
        )
    if "SubjectAlternativeNames" in data:
        import capo_acm.types.general_name_list

        out["subject_alternative_names"] = (
            capo_acm.types.general_name_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if "ExtendedKeyUsages" in data:
        import capo_acm.types.extended_key_usage_names

        out["extended_key_usages"] = (
            capo_acm.types.extended_key_usage_names.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if "KeyAlgorithm" in data:
        import capo_acm.types.key_algorithm

        out["key_algorithm"] = capo_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if "KeyUsages" in data:
        import capo_acm.types.key_usage_names

        out["key_usages"] = capo_acm.types.key_usage_names.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "NotAfter" in data:
        import capo_acm.types.t_stamp

        out["not_after"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if "NotBefore" in data:
        import capo_acm.types.t_stamp

        out["not_before"] = capo_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    return out
