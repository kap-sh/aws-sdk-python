"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterEndpoint(TypedDict, closed=True):
    address: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The DNS address of the cluster.</p>"""
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port that the database engine listens on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterEndpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterEndpoint:
    out: AwsRedshiftClusterEndpoint = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Port" in data:
        out["port"] = data["Port"]
    return out
