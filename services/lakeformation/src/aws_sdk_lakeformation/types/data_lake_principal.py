"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakePrincipal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_lake_principal_string


class DataLakePrincipal(TypedDict):
    data_lake_principal_identifier: NotRequired[
        "aws_sdk_lakeformation.types.data_lake_principal_string.DataLakePrincipalString"
    ]
    """<p>An identifier for the Lake Formation principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakePrincipal) -> dict:
    out: dict = {}
    if "data_lake_principal_identifier" in value:
        out["DataLakePrincipalIdentifier"] = value["data_lake_principal_identifier"]
    return out


def deserialize_json(data: dict) -> DataLakePrincipal:
    out: DataLakePrincipal = {}  # type: ignore[typeddict-item]
    if "DataLakePrincipalIdentifier" in data:
        out["data_lake_principal_identifier"] = data["DataLakePrincipalIdentifier"]
    return out
