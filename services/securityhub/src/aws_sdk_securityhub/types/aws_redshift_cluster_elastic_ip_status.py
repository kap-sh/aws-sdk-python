"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterElasticIpStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterElasticIpStatus(TypedDict, closed=True):
    elastic_ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The elastic IP address for the cluster.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the elastic IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterElasticIpStatus) -> dict:
    out: dict = {}
    if "elastic_ip" in value:
        out["ElasticIp"] = value["elastic_ip"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterElasticIpStatus:
    out: AwsRedshiftClusterElasticIpStatus = {}  # type: ignore[typeddict-item]
    if "ElasticIp" in data:
        out["elastic_ip"] = data["ElasticIp"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
