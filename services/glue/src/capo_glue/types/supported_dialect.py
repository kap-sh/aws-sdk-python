"""Generated from Smithy shape ``com.amazonaws.glue#SupportedDialect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.view_dialect
    import capo_glue.types.view_dialect_version_string


class SupportedDialect(TypedDict, closed=True):
    dialect: NotRequired["capo_glue.types.view_dialect.ViewDialect"]
    """<p>The dialect of the query engine.</p>"""
    dialect_version: NotRequired[
        "capo_glue.types.view_dialect_version_string.ViewDialectVersionString"
    ]
    """<p>The version of the dialect of the query engine. For example, 3.0.0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedDialect) -> dict:
    out: dict = {}
    if "dialect" in value:
        import capo_glue.types.view_dialect

        out["Dialect"] = capo_glue.types.view_dialect.serialize_aws_json_1_1(
            value["dialect"]
        )
    if "dialect_version" in value:
        out["DialectVersion"] = value["dialect_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedDialect:
    out: SupportedDialect = {}  # type: ignore[typeddict-item]
    if "Dialect" in data:
        import capo_glue.types.view_dialect

        out["dialect"] = capo_glue.types.view_dialect.deserialize_aws_json_1_1(
            data["Dialect"]
        )
    if "DialectVersion" in data:
        out["dialect_version"] = data["DialectVersion"]
    return out
