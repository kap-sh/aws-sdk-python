"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentVariant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_overrides
    import capo_amplifyuibuilder.types.component_variant_values


class ComponentVariant(TypedDict, closed=True):
    variant_values: NotRequired[
        "capo_amplifyuibuilder.types.component_variant_values.ComponentVariantValues"
    ]
    """<p>The combination of variants that comprise this variant. You can't specify <code>tags</code> as a valid property for <code>variantValues</code>.</p>"""
    overrides: NotRequired[
        "capo_amplifyuibuilder.types.component_overrides.ComponentOverrides"
    ]
    """<p>The properties of the component variant that can be overriden when customizing an instance of the component. You can't specify <code>tags</code> as a valid property for <code>overrides</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVariant) -> dict:
    out: dict = {}
    if "variant_values" in value:
        import capo_amplifyuibuilder.types.component_variant_values

        out["variantValues"] = (
            capo_amplifyuibuilder.types.component_variant_values.serialize_json(
                value["variant_values"]
            )
        )
    if "overrides" in value:
        import capo_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            capo_amplifyuibuilder.types.component_overrides.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentVariant:
    out: ComponentVariant = {}  # type: ignore[typeddict-item]
    if "variantValues" in data:
        import capo_amplifyuibuilder.types.component_variant_values

        out["variant_values"] = (
            capo_amplifyuibuilder.types.component_variant_values.deserialize_json(
                data["variantValues"]
            )
        )
    if "overrides" in data:
        import capo_amplifyuibuilder.types.component_overrides

        out["overrides"] = (
            capo_amplifyuibuilder.types.component_overrides.deserialize_json(
                data["overrides"]
            )
        )
    return out
