"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#SubjectNameFlagsV4``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SubjectNameFlagsV4(TypedDict):
    san_require_domain_dns: NotRequired["bool"]
    """<p>Include the domain DNS in the subject alternate name.</p>"""
    san_require_spn: NotRequired["bool"]
    """<p>Include the service principal name (SPN) in the subject alternate name.</p>"""
    san_require_directory_guid: NotRequired["bool"]
    """<p>Include the globally unique identifier (GUID) in the subject alternate name.</p>"""
    san_require_upn: NotRequired["bool"]
    """<p>Include the user principal name (UPN) in the subject alternate name.</p>"""
    san_require_email: NotRequired["bool"]
    """<p>Include the subject's email in the subject alternate name.</p>"""
    san_require_dns: NotRequired["bool"]
    """<p>Include the DNS in the subject alternate name.</p>"""
    require_dns_as_cn: NotRequired["bool"]
    """<p>Include the DNS as common name in the subject name.</p>"""
    require_email: NotRequired["bool"]
    """<p>Include the subject's email in the subject name.</p>"""
    require_common_name: NotRequired["bool"]
    """<p>Include the common name in the subject name.</p>"""
    require_directory_path: NotRequired["bool"]
    """<p>Include the directory path in the subject name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectNameFlagsV4) -> dict:
    out: dict = {}
    if "san_require_domain_dns" in value:
        out["SanRequireDomainDns"] = value["san_require_domain_dns"]
    if "san_require_spn" in value:
        out["SanRequireSpn"] = value["san_require_spn"]
    if "san_require_directory_guid" in value:
        out["SanRequireDirectoryGuid"] = value["san_require_directory_guid"]
    if "san_require_upn" in value:
        out["SanRequireUpn"] = value["san_require_upn"]
    if "san_require_email" in value:
        out["SanRequireEmail"] = value["san_require_email"]
    if "san_require_dns" in value:
        out["SanRequireDns"] = value["san_require_dns"]
    if "require_dns_as_cn" in value:
        out["RequireDnsAsCn"] = value["require_dns_as_cn"]
    if "require_email" in value:
        out["RequireEmail"] = value["require_email"]
    if "require_common_name" in value:
        out["RequireCommonName"] = value["require_common_name"]
    if "require_directory_path" in value:
        out["RequireDirectoryPath"] = value["require_directory_path"]
    return out


def deserialize_json(data: dict) -> SubjectNameFlagsV4:
    out: SubjectNameFlagsV4 = {}  # type: ignore[typeddict-item]
    if "SanRequireDomainDns" in data:
        out["san_require_domain_dns"] = data["SanRequireDomainDns"]
    if "SanRequireSpn" in data:
        out["san_require_spn"] = data["SanRequireSpn"]
    if "SanRequireDirectoryGuid" in data:
        out["san_require_directory_guid"] = data["SanRequireDirectoryGuid"]
    if "SanRequireUpn" in data:
        out["san_require_upn"] = data["SanRequireUpn"]
    if "SanRequireEmail" in data:
        out["san_require_email"] = data["SanRequireEmail"]
    if "SanRequireDns" in data:
        out["san_require_dns"] = data["SanRequireDns"]
    if "RequireDnsAsCn" in data:
        out["require_dns_as_cn"] = data["RequireDnsAsCn"]
    if "RequireEmail" in data:
        out["require_email"] = data["RequireEmail"]
    if "RequireCommonName" in data:
        out["require_common_name"] = data["RequireCommonName"]
    if "RequireDirectoryPath" in data:
        out["require_directory_path"] = data["RequireDirectoryPath"]
    return out
