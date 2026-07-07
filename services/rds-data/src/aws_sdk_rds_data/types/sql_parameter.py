"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.field
    import aws_sdk_rds_data.types.parameter_name
    import aws_sdk_rds_data.types.type_hint


class SqlParameter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_rds_data.types.parameter_name.ParameterName"]
    """<p>The name of the parameter.</p>"""
    value: NotRequired["aws_sdk_rds_data.types.field.Field"]
    """<p>The value of the parameter.</p>"""
    type_hint: NotRequired["aws_sdk_rds_data.types.type_hint.TypeHint"]
    """<p>A hint that specifies the correct object type for data type mapping. Possible values are as follows:</p> <ul> <li> <p> <code>DATE</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>DATE</code> type to the database. The accepted format is <code>YYYY-MM-DD</code>.</p> </li> <li> <p> <code>DECIMAL</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>DECIMAL</code> type to the database.</p> </li> <li> <p> <code>JSON</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>JSON</code> type to the database.</p> </li> <li> <p> <code>TIME</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>TIME</code> type to the database. The accepted format is <code>HH:MM:SS[.FFF]</code>.</p> </li> <li> <p> <code>TIMESTAMP</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>TIMESTAMP</code> type to the database. The accepted format is <code>YYYY-MM-DD HH:MM:SS[.FFF]</code>.</p> </li> <li> <p> <code>UUID</code> - The corresponding <code>String</code> parameter value is sent as an object of <code>UUID</code> type to the database. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqlParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        import aws_sdk_rds_data.types.field

        out["value"] = aws_sdk_rds_data.types.field.serialize_json(value["value"])
    if "type_hint" in value:
        import aws_sdk_rds_data.types.type_hint

        out["typeHint"] = aws_sdk_rds_data.types.type_hint.serialize_json(
            value["type_hint"]
        )
    return out


def deserialize_json(data: dict) -> SqlParameter:
    out: SqlParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        import aws_sdk_rds_data.types.field

        out["value"] = aws_sdk_rds_data.types.field.deserialize_json(data["value"])
    if "typeHint" in data:
        import aws_sdk_rds_data.types.type_hint

        out["type_hint"] = aws_sdk_rds_data.types.type_hint.deserialize_json(
            data["typeHint"]
        )
    return out
