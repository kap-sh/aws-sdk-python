"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CompositeSliConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.composite_sli_components
    import capo_application_signals.types.selection_config


class CompositeSliConfig(TypedDict, closed=True):
    selection_config: "capo_application_signals.types.selection_config.SelectionConfig"
    """<p>Specifies how operations are selected for this service-level SLO. Operations can be selected explicitly by listing them, by specifying a prefix to match operation names, or by providing a regular expression pattern.</p>"""
    components: NotRequired[
        "capo_application_signals.types.composite_sli_components.CompositeSliComponents"
    ]
    """<p>The list of operations included in this composite SLI. You must specify between 2 and 20 components. Each component is a <code>CompositeSliComponent</code> that identifies a single operation by its <code>OperationName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSliConfig) -> dict:
    out: dict = {}
    import capo_application_signals.types.selection_config

    out["SelectionConfig"] = (
        capo_application_signals.types.selection_config.serialize_json(
            value["selection_config"]
        )
    )
    if "components" in value:
        import capo_application_signals.types.composite_sli_components

        out["Components"] = (
            capo_application_signals.types.composite_sli_components.serialize_json(
                value["components"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompositeSliConfig:
    out: CompositeSliConfig = {}  # type: ignore[typeddict-item]
    if "SelectionConfig" in data:
        import capo_application_signals.types.selection_config

        out["selection_config"] = (
            capo_application_signals.types.selection_config.deserialize_json(
                data["SelectionConfig"]
            )
        )
    else:
        raise DeserializationError("CompositeSliConfig.selection_config required")
    if "Components" in data:
        import capo_application_signals.types.composite_sli_components

        out["components"] = (
            capo_application_signals.types.composite_sli_components.deserialize_json(
                data["Components"]
            )
        )
    return out
