"""Generated from Smithy shape ``com.amazonaws.dataexchange#RedshiftDataShareDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string


class RedshiftDataShareDetails(TypedDict, closed=True):
    arn: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The ARN of the underlying Redshift data share that is being affected by this notification.</p>"""
    database: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The database name in the Redshift data share that is being affected by this notification.</p>"""
    function: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A function name in the Redshift database that is being affected by this notification.</p>"""
    table: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A table name in the Redshift database that is being affected by this notification.</p>"""
    schema: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A schema name in the Redshift database that is being affected by this notification.</p>"""
    view: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>A view name in the Redshift database that is being affected by this notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftDataShareDetails) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Database"] = value["database"]
    if "function" in value:
        out["Function"] = value["function"]
    if "table" in value:
        out["Table"] = value["table"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "view" in value:
        out["View"] = value["view"]
    return out


def deserialize_json(data: dict) -> RedshiftDataShareDetails:
    out: RedshiftDataShareDetails = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("RedshiftDataShareDetails.arn required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftDataShareDetails.database required")
    if "Function" in data:
        out["function"] = data["Function"]
    if "Table" in data:
        out["table"] = data["Table"]
    if "Schema" in data:
        out["schema"] = data["Schema"]
    if "View" in data:
        out["view"] = data["View"]
    return out
