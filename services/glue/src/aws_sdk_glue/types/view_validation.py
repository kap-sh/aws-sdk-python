"""Generated from Smithy shape ``com.amazonaws.glue#ViewValidation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.resource_state
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.view_dialect
    import aws_sdk_glue.types.view_dialect_version_string
    import aws_sdk_glue.types.view_text_string


class ViewValidation(TypedDict):
    dialect: NotRequired["aws_sdk_glue.types.view_dialect.ViewDialect"]
    """<p>The dialect of the query engine.</p>"""
    dialect_version: NotRequired[
        "aws_sdk_glue.types.view_dialect_version_string.ViewDialectVersionString"
    ]
    """<p>The version of the dialect of the query engine. For example, 3.0.0.</p>"""
    view_validation_text: NotRequired[
        "aws_sdk_glue.types.view_text_string.ViewTextString"
    ]
    """<p>The <code>SELECT</code> query that defines the view, as provided by the customer.</p>"""
    update_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time of the last update.</p>"""
    state: NotRequired["aws_sdk_glue.types.resource_state.ResourceState"]
    """<p>The state of the validation.</p>"""
    error: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>An error associated with the validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewValidation) -> dict:
    out: dict = {}
    if "dialect" in value:
        import aws_sdk_glue.types.view_dialect

        out["Dialect"] = aws_sdk_glue.types.view_dialect.serialize_aws_json_1_1(
            value["dialect"]
        )
    if "dialect_version" in value:
        out["DialectVersion"] = value["dialect_version"]
    if "view_validation_text" in value:
        out["ViewValidationText"] = value["view_validation_text"]
    if "update_time" in value:
        import aws_sdk_glue.types.timestamp

        out["UpdateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    if "state" in value:
        import aws_sdk_glue.types.resource_state

        out["State"] = aws_sdk_glue.types.resource_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "error" in value:
        import aws_sdk_glue.types.error_detail

        out["Error"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewValidation:
    out: ViewValidation = {}  # type: ignore[typeddict-item]
    if "Dialect" in data:
        import aws_sdk_glue.types.view_dialect

        out["dialect"] = aws_sdk_glue.types.view_dialect.deserialize_aws_json_1_1(
            data["Dialect"]
        )
    if "DialectVersion" in data:
        out["dialect_version"] = data["DialectVersion"]
    if "ViewValidationText" in data:
        out["view_validation_text"] = data["ViewValidationText"]
    if "UpdateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["update_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    if "State" in data:
        import aws_sdk_glue.types.resource_state

        out["state"] = aws_sdk_glue.types.resource_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Error" in data:
        import aws_sdk_glue.types.error_detail

        out["error"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["Error"]
        )
    return out
