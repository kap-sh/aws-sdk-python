"""Generated from Smithy shape ``com.amazonaws.acmpca#GeneralName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.asn1_subject
    import capo_acm_pca.types.custom_object_identifier
    import capo_acm_pca.types.edi_party_name
    import capo_acm_pca.types.other_name
    import capo_acm_pca.types.string39
    import capo_acm_pca.types.string253
    import capo_acm_pca.types.string256


class GeneralName(TypedDict, closed=True):
    other_name: NotRequired["capo_acm_pca.types.other_name.OtherName"]
    """<p>Represents <code>GeneralName</code> using an <code>OtherName</code> object.</p>"""
    rfc822_name: NotRequired["capo_acm_pca.types.string256.String256"]
    r"""<p>Represents <code>GeneralName</code> as an <a href=\"https://datatracker.ietf.org/doc/html/rfc822\">RFC 822</a> email address.</p>"""
    dns_name: NotRequired["capo_acm_pca.types.string253.String253"]
    """<p>Represents <code>GeneralName</code> as a DNS name.</p>"""
    directory_name: NotRequired["capo_acm_pca.types.asn1_subject.ASN1Subject"]
    edi_party_name: NotRequired["capo_acm_pca.types.edi_party_name.EdiPartyName"]
    """<p>Represents <code>GeneralName</code> as an <code>EdiPartyName</code> object.</p>"""
    uniform_resource_identifier: NotRequired["capo_acm_pca.types.string253.String253"]
    """<p>Represents <code>GeneralName</code> as a URI.</p>"""
    ip_address: NotRequired["capo_acm_pca.types.string39.String39"]
    """<p>Represents <code>GeneralName</code> as an IPv4 or IPv6 address.</p>"""
    registered_id: NotRequired[
        "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    ]
    """<p> Represents <code>GeneralName</code> as an object identifier (OID).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralName) -> dict:
    out: dict = {}
    if "other_name" in value:
        import capo_acm_pca.types.other_name

        out["OtherName"] = capo_acm_pca.types.other_name.serialize_aws_json_1_1(
            value["other_name"]
        )
    if "rfc822_name" in value:
        out["Rfc822Name"] = value["rfc822_name"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "directory_name" in value:
        import capo_acm_pca.types.asn1_subject

        out["DirectoryName"] = capo_acm_pca.types.asn1_subject.serialize_aws_json_1_1(
            value["directory_name"]
        )
    if "edi_party_name" in value:
        import capo_acm_pca.types.edi_party_name

        out["EdiPartyName"] = capo_acm_pca.types.edi_party_name.serialize_aws_json_1_1(
            value["edi_party_name"]
        )
    if "uniform_resource_identifier" in value:
        out["UniformResourceIdentifier"] = value["uniform_resource_identifier"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "registered_id" in value:
        out["RegisteredId"] = value["registered_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GeneralName:
    out: GeneralName = {}  # type: ignore[typeddict-item]
    if "OtherName" in data:
        import capo_acm_pca.types.other_name

        out["other_name"] = capo_acm_pca.types.other_name.deserialize_aws_json_1_1(
            data["OtherName"]
        )
    if "Rfc822Name" in data:
        out["rfc822_name"] = data["Rfc822Name"]
    if "DnsName" in data:
        out["dns_name"] = data["DnsName"]
    if "DirectoryName" in data:
        import capo_acm_pca.types.asn1_subject

        out["directory_name"] = (
            capo_acm_pca.types.asn1_subject.deserialize_aws_json_1_1(
                data["DirectoryName"]
            )
        )
    if "EdiPartyName" in data:
        import capo_acm_pca.types.edi_party_name

        out["edi_party_name"] = (
            capo_acm_pca.types.edi_party_name.deserialize_aws_json_1_1(
                data["EdiPartyName"]
            )
        )
    if "UniformResourceIdentifier" in data:
        out["uniform_resource_identifier"] = data["UniformResourceIdentifier"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "RegisteredId" in data:
        out["registered_id"] = data["RegisteredId"]
    return out
