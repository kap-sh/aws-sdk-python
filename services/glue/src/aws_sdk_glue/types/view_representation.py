"""Generated from Smithy shape ``com.amazonaws.glue#ViewRepresentation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.view_dialect
    import aws_sdk_glue.types.view_dialect_version_string
    import aws_sdk_glue.types.view_text_string


class ViewRepresentation(TypedDict, closed=True):
    dialect: NotRequired["aws_sdk_glue.types.view_dialect.ViewDialect"]
    """<p>The dialect of the query engine.</p>"""
    dialect_version: NotRequired[
        "aws_sdk_glue.types.view_dialect_version_string.ViewDialectVersionString"
    ]
    """<p>The version of the dialect of the query engine. For example, 3.0.0.</p>"""
    view_original_text: NotRequired[
        "aws_sdk_glue.types.view_text_string.ViewTextString"
    ]
    """<p>The <code>SELECT</code> query provided by the customer during <code>CREATE VIEW DDL</code>. This SQL is not used during a query on a view (<code>ViewExpandedText</code> is used instead). <code>ViewOriginalText</code> is used for cases like <code>SHOW CREATE VIEW</code> where users want to see the original DDL command that created the view.</p>"""
    view_expanded_text: NotRequired[
        "aws_sdk_glue.types.view_text_string.ViewTextString"
    ]
    """<p>The expanded SQL for the view. This SQL is used by engines while processing a query on a view. Engines may perform operations during view creation to transform <code>ViewOriginalText</code> to <code>ViewExpandedText</code>. For example:</p> <ul> <li> <p>Fully qualified identifiers: <code>SELECT * from table1 -> SELECT * from db1.table1</code> </p> </li> </ul>"""
    validation_connection: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the connection to be used to validate the specific representation of the view.</p>"""
    is_stale: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Dialects marked as stale are no longer valid and must be updated before they can be queried in their respective query engines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewRepresentation) -> dict:
    out: dict = {}
    if "dialect" in value:
        import aws_sdk_glue.types.view_dialect

        out["Dialect"] = aws_sdk_glue.types.view_dialect.serialize_aws_json_1_1(
            value["dialect"]
        )
    if "dialect_version" in value:
        out["DialectVersion"] = value["dialect_version"]
    if "view_original_text" in value:
        out["ViewOriginalText"] = value["view_original_text"]
    if "view_expanded_text" in value:
        out["ViewExpandedText"] = value["view_expanded_text"]
    if "validation_connection" in value:
        out["ValidationConnection"] = value["validation_connection"]
    if "is_stale" in value:
        out["IsStale"] = value["is_stale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewRepresentation:
    out: ViewRepresentation = {}  # type: ignore[typeddict-item]
    if "Dialect" in data:
        import aws_sdk_glue.types.view_dialect

        out["dialect"] = aws_sdk_glue.types.view_dialect.deserialize_aws_json_1_1(
            data["Dialect"]
        )
    if "DialectVersion" in data:
        out["dialect_version"] = data["DialectVersion"]
    if "ViewOriginalText" in data:
        out["view_original_text"] = data["ViewOriginalText"]
    if "ViewExpandedText" in data:
        out["view_expanded_text"] = data["ViewExpandedText"]
    if "ValidationConnection" in data:
        out["validation_connection"] = data["ValidationConnection"]
    if "IsStale" in data:
        out["is_stale"] = data["IsStale"]
    return out
