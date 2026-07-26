"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToProtect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_protect_keys
    import capo_wafv2.types.field_to_protect_type


class FieldToProtect(TypedDict, closed=True):
    field_type: "capo_wafv2.types.field_to_protect_type.FieldToProtectType"
    """<p>Specifies the web request component type to protect. </p>"""
    field_keys: NotRequired["capo_wafv2.types.field_to_protect_keys.FieldToProtectKeys"]
    """<p>Specifies the keys to protect for the specified field type. If you don't specify any key, then all keys for the field type are protected. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldToProtect) -> dict:
    out: dict = {}
    import capo_wafv2.types.field_to_protect_type

    out["FieldType"] = capo_wafv2.types.field_to_protect_type.serialize_aws_json_1_1(
        value["field_type"]
    )
    if "field_keys" in value:
        import capo_wafv2.types.field_to_protect_keys

        out["FieldKeys"] = (
            capo_wafv2.types.field_to_protect_keys.serialize_aws_json_1_1(
                value["field_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldToProtect:
    out: FieldToProtect = {}  # type: ignore[typeddict-item]
    if "FieldType" in data:
        import capo_wafv2.types.field_to_protect_type

        out["field_type"] = (
            capo_wafv2.types.field_to_protect_type.deserialize_aws_json_1_1(
                data["FieldType"]
            )
        )
    else:
        raise DeserializationError("FieldToProtect.field_type required")
    if "FieldKeys" in data:
        import capo_wafv2.types.field_to_protect_keys

        out["field_keys"] = (
            capo_wafv2.types.field_to_protect_keys.deserialize_aws_json_1_1(
                data["FieldKeys"]
            )
        )
    return out
