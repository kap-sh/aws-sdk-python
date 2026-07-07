"""Generated from Smithy shape ``com.amazonaws.inspector#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector.types.scope_type
    import aws_sdk_inspector.types.scope_value


class Scope(TypedDict, closed=True):
    key: NotRequired["aws_sdk_inspector.types.scope_type.ScopeType"]
    """<p>The type of the scope.</p>"""
    value: NotRequired["aws_sdk_inspector.types.scope_value.ScopeValue"]
    """<p>The resource identifier for the specified scope type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Scope) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_inspector.types.scope_type

        out["key"] = aws_sdk_inspector.types.scope_type.serialize_aws_json_1_1(
            value["key"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_inspector.types.scope_type

        out["key"] = aws_sdk_inspector.types.scope_type.deserialize_aws_json_1_1(
            data["key"]
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
