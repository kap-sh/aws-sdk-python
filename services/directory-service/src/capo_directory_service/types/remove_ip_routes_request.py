"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveIpRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.cidr_ips
    import capo_directory_service.types.cidr_ipv6s
    import capo_directory_service.types.directory_id


class RemoveIpRoutesRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier (ID) of the directory from which you want to remove the IP addresses.</p>"""
    cidr_ips: "capo_directory_service.types.cidr_ips.CidrIps"
    """<p>IP address blocks that you want to remove.</p>"""
    cidr_ipv6s: NotRequired["capo_directory_service.types.cidr_ipv6s.CidrIpv6s"]
    """<p>IPv6 address blocks that you want to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveIpRoutesRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.cidr_ips

    out["CidrIps"] = capo_directory_service.types.cidr_ips.serialize_aws_json_1_1(
        value.get("cidr_ips", [])
    )
    if "cidr_ipv6s" in value:
        import capo_directory_service.types.cidr_ipv6s

        out["CidrIpv6s"] = (
            capo_directory_service.types.cidr_ipv6s.serialize_aws_json_1_1(
                value["cidr_ipv6s"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveIpRoutesRequest:
    out: RemoveIpRoutesRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("RemoveIpRoutesRequest.directory_id required")
    if "CidrIps" in data:
        import capo_directory_service.types.cidr_ips

        out["cidr_ips"] = (
            capo_directory_service.types.cidr_ips.deserialize_aws_json_1_1(
                data["CidrIps"]
            )
        )
    else:
        out["cidr_ips"] = []
    if "CidrIpv6s" in data:
        import capo_directory_service.types.cidr_ipv6s

        out["cidr_ipv6s"] = (
            capo_directory_service.types.cidr_ipv6s.deserialize_aws_json_1_1(
                data["CidrIpv6s"]
            )
        )
    return out
