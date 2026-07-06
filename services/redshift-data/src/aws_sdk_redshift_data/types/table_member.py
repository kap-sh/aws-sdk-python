"""Generated from Smithy shape ``com.amazonaws.redshiftdata#TableMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string


class TableMember(TypedDict, closed=True):
    name: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The name of the table. </p>"""
    type: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The type of the table. Possible values include TABLE, VIEW, SYSTEM TABLE, GLOBAL TEMPORARY, LOCAL TEMPORARY, ALIAS, and SYNONYM. </p>"""
    schema: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The schema containing the table. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableMember) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableMember:
    out: TableMember = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "schema" in data:
        out["schema"] = data["schema"]
    return out
