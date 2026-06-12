"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_runtime
    import aws_sdk_cloudfront.types.key_value_store_associations
    import aws_sdk_cloudfront.types.string


class FunctionConfig(TypedDict):
    comment: "aws_sdk_cloudfront.types.string.string"
    """<p>A comment to describe the function.</p>"""
    runtime: "aws_sdk_cloudfront.types.function_runtime.FunctionRuntime"
    """<p>The function's runtime environment version.</p>"""
    key_value_store_associations: NotRequired[
        "aws_sdk_cloudfront.types.key_value_store_associations.KeyValueStoreAssociations"
    ]
    """<p>The configuration for the key value store associations.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FunctionConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Comment").text = str(value["comment"])
    import aws_sdk_cloudfront.types.function_runtime

    aws_sdk_cloudfront.types.function_runtime.serialize_xml(
        value["runtime"], el, "Runtime"
    )
    if "key_value_store_associations" in value:
        import aws_sdk_cloudfront.types.key_value_store_associations

        aws_sdk_cloudfront.types.key_value_store_associations.serialize_xml(
            value["key_value_store_associations"], el, "KeyValueStoreAssociations"
        )


def deserialize_xml(el: Element) -> FunctionConfig:
    out: FunctionConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("FunctionConfig.comment required")
    child_runtime = el.find("Runtime")
    if child_runtime is not None:
        import aws_sdk_cloudfront.types.function_runtime

        out["runtime"] = aws_sdk_cloudfront.types.function_runtime.deserialize_xml(
            child_runtime
        )
    else:
        raise DeserializationError("FunctionConfig.runtime required")
    child_key_value_store_associations = el.find("KeyValueStoreAssociations")
    if child_key_value_store_associations is not None:
        import aws_sdk_cloudfront.types.key_value_store_associations

        out["key_value_store_associations"] = (
            aws_sdk_cloudfront.types.key_value_store_associations.deserialize_xml(
                child_key_value_store_associations
            )
        )
    return out
