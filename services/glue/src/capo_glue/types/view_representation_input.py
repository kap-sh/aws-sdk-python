"""Generated from Smithy shape ``com.amazonaws.glue#ViewRepresentationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.view_dialect
    import capo_glue.types.view_dialect_version_string
    import capo_glue.types.view_text_string


class ViewRepresentationInput(TypedDict, closed=True):
    dialect: NotRequired["capo_glue.types.view_dialect.ViewDialect"]
    """<p>A parameter that specifies the engine type of a specific representation.</p>"""
    dialect_version: NotRequired[
        "capo_glue.types.view_dialect_version_string.ViewDialectVersionString"
    ]
    """<p>A parameter that specifies the version of the engine of a specific representation.</p>"""
    view_original_text: NotRequired["capo_glue.types.view_text_string.ViewTextString"]
    """<p>A string that represents the original SQL query that describes the view.</p>"""
    validation_connection: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the connection to be used to validate the specific representation of the view.</p>"""
    view_expanded_text: NotRequired["capo_glue.types.view_text_string.ViewTextString"]
    """<p>A string that represents the SQL query that describes the view with expanded resource ARNs</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewRepresentationInput) -> dict:
    out: dict = {}
    if "dialect" in value:
        import capo_glue.types.view_dialect

        out["Dialect"] = capo_glue.types.view_dialect.serialize_aws_json_1_1(
            value["dialect"]
        )
    if "dialect_version" in value:
        out["DialectVersion"] = value["dialect_version"]
    if "view_original_text" in value:
        out["ViewOriginalText"] = value["view_original_text"]
    if "validation_connection" in value:
        out["ValidationConnection"] = value["validation_connection"]
    if "view_expanded_text" in value:
        out["ViewExpandedText"] = value["view_expanded_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewRepresentationInput:
    out: ViewRepresentationInput = {}  # type: ignore[typeddict-item]
    if "Dialect" in data:
        import capo_glue.types.view_dialect

        out["dialect"] = capo_glue.types.view_dialect.deserialize_aws_json_1_1(
            data["Dialect"]
        )
    if "DialectVersion" in data:
        out["dialect_version"] = data["DialectVersion"]
    if "ViewOriginalText" in data:
        out["view_original_text"] = data["ViewOriginalText"]
    if "ValidationConnection" in data:
        out["validation_connection"] = data["ValidationConnection"]
    if "ViewExpandedText" in data:
        out["view_expanded_text"] = data["ViewExpandedText"]
    return out
