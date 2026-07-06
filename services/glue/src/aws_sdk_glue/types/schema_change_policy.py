"""Generated from Smithy shape ``com.amazonaws.glue#SchemaChangePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.delete_behavior
    import aws_sdk_glue.types.update_behavior


class SchemaChangePolicy(TypedDict, closed=True):
    update_behavior: NotRequired["aws_sdk_glue.types.update_behavior.UpdateBehavior"]
    """<p>The update behavior when the crawler finds a changed schema.</p>"""
    delete_behavior: NotRequired["aws_sdk_glue.types.delete_behavior.DeleteBehavior"]
    """<p>The deletion behavior when the crawler finds a deleted object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaChangePolicy) -> dict:
    out: dict = {}
    if "update_behavior" in value:
        import aws_sdk_glue.types.update_behavior

        out["UpdateBehavior"] = (
            aws_sdk_glue.types.update_behavior.serialize_aws_json_1_1(
                value["update_behavior"]
            )
        )
    if "delete_behavior" in value:
        import aws_sdk_glue.types.delete_behavior

        out["DeleteBehavior"] = (
            aws_sdk_glue.types.delete_behavior.serialize_aws_json_1_1(
                value["delete_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaChangePolicy:
    out: SchemaChangePolicy = {}  # type: ignore[typeddict-item]
    if "UpdateBehavior" in data:
        import aws_sdk_glue.types.update_behavior

        out["update_behavior"] = (
            aws_sdk_glue.types.update_behavior.deserialize_aws_json_1_1(
                data["UpdateBehavior"]
            )
        )
    if "DeleteBehavior" in data:
        import aws_sdk_glue.types.delete_behavior

        out["delete_behavior"] = (
            aws_sdk_glue.types.delete_behavior.deserialize_aws_json_1_1(
                data["DeleteBehavior"]
            )
        )
    return out
