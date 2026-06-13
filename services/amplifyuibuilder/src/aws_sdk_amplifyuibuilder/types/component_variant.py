"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentVariant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_overrides
    import aws_sdk_amplifyuibuilder.types.component_variant_values


class ComponentVariant(TypedDict):
    variant_values: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_variant_values.ComponentVariantValues"
    ]
    """<p>The combination of variants that comprise this variant. You can't specify <code>tags</code> as a valid property for <code>variantValues</code>.</p>"""
    overrides: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    ]
    """<p>The properties of the component variant that can be overriden when customizing an instance of the component. You can't specify <code>tags</code> as a valid property for <code>overrides</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVariant) -> dict:
    out: dict = {}
    if "variant_values" in value:
        import aws_sdk_amplifyuibuilder.types.component_variant_values

        out["variantValues"] = (
            aws_sdk_amplifyuibuilder.types.component_variant_values.serialize_json(
                value["variant_values"]
            )
        )
    if "overrides" in value:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentVariant:
    out: ComponentVariant = {}  # type: ignore[typeddict-item]
    if "variantValues" in data:
        import aws_sdk_amplifyuibuilder.types.component_variant_values

        out["variant_values"] = (
            aws_sdk_amplifyuibuilder.types.component_variant_values.deserialize_json(
                data["variantValues"]
            )
        )
    if "overrides" in data:
        import aws_sdk_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            aws_sdk_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    return out
