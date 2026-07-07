"""Generated from Smithy shape ``com.amazonaws.iam#ContextEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.context_key_name_type
    import aws_sdk_iam.types.context_key_type_enum
    import aws_sdk_iam.types.context_key_value_list_type


class ContextEntry(TypedDict, closed=True):
    context_key_name: NotRequired[
        "aws_sdk_iam.types.context_key_name_type.ContextKeyNameType"
    ]
    """<p>The full name of a condition context key, including the service prefix. For example, <code>aws:SourceIp</code> or <code>s3:VersionId</code>.</p>"""
    context_key_values: NotRequired[
        "aws_sdk_iam.types.context_key_value_list_type.ContextKeyValueListType"
    ]
    """<p>The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a <code>Condition</code> element in an input policy.</p>"""
    context_key_type: NotRequired[
        "aws_sdk_iam.types.context_key_type_enum.ContextKeyTypeEnum"
    ]
    """<p>The data type of the value (or values) specified in the <code>ContextKeyValues</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ContextEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "context_key_name" in value:
        pairs.append((f"{prefix}.ContextKeyName", str(value["context_key_name"])))
    if "context_key_values" in value:
        import aws_sdk_iam.types.context_key_value_list_type

        aws_sdk_iam.types.context_key_value_list_type.serialize_query(
            value["context_key_values"], pairs, f"{prefix}.ContextKeyValues"
        )
    if "context_key_type" in value:
        import aws_sdk_iam.types.context_key_type_enum

        aws_sdk_iam.types.context_key_type_enum.serialize_query(
            value["context_key_type"], pairs, f"{prefix}.ContextKeyType"
        )


def deserialize_query(el: Element) -> ContextEntry:
    out: ContextEntry = {}  # type: ignore[typeddict-item]
    child_context_key_name = el.find("ContextKeyName")
    if child_context_key_name is not None:
        out["context_key_name"] = str(child_context_key_name.text or "")
    child_context_key_values = el.find("ContextKeyValues")
    if child_context_key_values is not None:
        import aws_sdk_iam.types.context_key_value_list_type

        out["context_key_values"] = (
            aws_sdk_iam.types.context_key_value_list_type.deserialize_query(
                child_context_key_values
            )
        )
    child_context_key_type = el.find("ContextKeyType")
    if child_context_key_type is not None:
        import aws_sdk_iam.types.context_key_type_enum

        out["context_key_type"] = (
            aws_sdk_iam.types.context_key_type_enum.deserialize_query(
                child_context_key_type
            )
        )
    return out
