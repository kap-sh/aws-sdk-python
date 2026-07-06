"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string


class RelationalDatabaseEndpoint(TypedDict, closed=True):
    port: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>Specifies the port that the database is listening on.</p>"""
    address: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the DNS address of the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseEndpoint) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    if "address" in value:
        out["address"] = value["address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseEndpoint:
    out: RelationalDatabaseEndpoint = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    if "address" in data:
        out["address"] = data["address"]
    return out
