"""Generated from Smithy shape ``com.amazonaws.glue#DataLakePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_lake_principal_string


class DataLakePrincipal(TypedDict, closed=True):
    data_lake_principal_identifier: NotRequired[
        "aws_sdk_glue.types.data_lake_principal_string.DataLakePrincipalString"
    ]
    """<p>An identifier for the Lake Formation principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataLakePrincipal) -> dict:
    out: dict = {}
    if "data_lake_principal_identifier" in value:
        out["DataLakePrincipalIdentifier"] = value["data_lake_principal_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataLakePrincipal:
    out: DataLakePrincipal = {}  # type: ignore[typeddict-item]
    if "DataLakePrincipalIdentifier" in data:
        out["data_lake_principal_identifier"] = data["DataLakePrincipalIdentifier"]
    return out
