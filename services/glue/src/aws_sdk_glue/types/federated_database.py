"""Generated from Smithy shape ``com.amazonaws.glue#FederatedDatabase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.federation_identifier
    import aws_sdk_glue.types.name_string


class FederatedDatabase(TypedDict):
    identifier: NotRequired[
        "aws_sdk_glue.types.federation_identifier.FederationIdentifier"
    ]
    """<p>A unique identifier for the federated database.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the connection to the external metastore.</p>"""
    connection_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The type of connection used to access the federated database, such as JDBC, ODBC, or other supported connection protocols.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederatedDatabase) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederatedDatabase:
    out: FederatedDatabase = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    return out
