"""Generated from Smithy shape ``com.amazonaws.glue#FederatedTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.federation_identifier
    import aws_sdk_glue.types.name_string


class FederatedTable(TypedDict):
    identifier: NotRequired[
        "aws_sdk_glue.types.federation_identifier.FederationIdentifier"
    ]
    """<p>A unique identifier for the federated table.</p>"""
    database_identifier: NotRequired[
        "aws_sdk_glue.types.federation_identifier.FederationIdentifier"
    ]
    """<p>A unique identifier for the federated database.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the connection to the external metastore.</p>"""
    connection_type: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The type of connection used to access the federated table, specifying the protocol or method for connecting to the external data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederatedTable) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "database_identifier" in value:
        out["DatabaseIdentifier"] = value["database_identifier"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_type" in value:
        out["ConnectionType"] = value["connection_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederatedTable:
    out: FederatedTable = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "DatabaseIdentifier" in data:
        out["database_identifier"] = data["DatabaseIdentifier"]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    return out
