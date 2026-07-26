"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.data_lake_principal_string


class DataLakePrincipal(TypedDict, closed=True):
    data_lake_principal_identifier: NotRequired[
        "capo_lakeformation.types.data_lake_principal_string.DataLakePrincipalString"
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
