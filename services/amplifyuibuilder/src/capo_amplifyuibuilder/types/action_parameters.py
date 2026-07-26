"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ActionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_properties
    import capo_amplifyuibuilder.types.component_property
    import capo_amplifyuibuilder.types.mutation_action_set_state_parameter

ActionParameters = TypedDict(
    "ActionParameters",
    {
        "type": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "url": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "anchor": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "target": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "global": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "model": NotRequired["str"],
        "id": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "fields": NotRequired[
            "capo_amplifyuibuilder.types.component_properties.ComponentProperties"
        ],
        "state": NotRequired[
            "capo_amplifyuibuilder.types.mutation_action_set_state_parameter.MutationActionSetStateParameter"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ActionParameters) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_amplifyuibuilder.types.component_property

        out["type"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["type"]
        )
    if "url" in value:
        import capo_amplifyuibuilder.types.component_property

        out["url"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["url"]
        )
    if "anchor" in value:
        import capo_amplifyuibuilder.types.component_property

        out["anchor"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["anchor"]
        )
    if "target" in value:
        import capo_amplifyuibuilder.types.component_property

        out["target"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["target"]
        )
    if "global" in value:
        import capo_amplifyuibuilder.types.component_property

        out["global"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["global"]
        )
    if "model" in value:
        out["model"] = value["model"]
    if "id" in value:
        import capo_amplifyuibuilder.types.component_property

        out["id"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["id"]
        )
    if "fields" in value:
        import capo_amplifyuibuilder.types.component_properties

        out["fields"] = capo_amplifyuibuilder.types.component_properties.serialize_json(
            value["fields"]
        )
    if "state" in value:
        import capo_amplifyuibuilder.types.mutation_action_set_state_parameter

        out["state"] = (
            capo_amplifyuibuilder.types.mutation_action_set_state_parameter.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActionParameters:
    out: ActionParameters = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_amplifyuibuilder.types.component_property

        out["type"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["type"]
        )
    if "url" in data:
        import capo_amplifyuibuilder.types.component_property

        out["url"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["url"]
        )
    if "anchor" in data:
        import capo_amplifyuibuilder.types.component_property

        out["anchor"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["anchor"]
        )
    if "target" in data:
        import capo_amplifyuibuilder.types.component_property

        out["target"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["target"]
        )
    if "global" in data:
        import capo_amplifyuibuilder.types.component_property

        out["global"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["global"]
        )
    if "model" in data:
        out["model"] = data["model"]
    if "id" in data:
        import capo_amplifyuibuilder.types.component_property

        out["id"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["id"]
        )
    if "fields" in data:
        import capo_amplifyuibuilder.types.component_properties

        out["fields"] = (
            capo_amplifyuibuilder.types.component_properties.deserialize_json(
                data["fields"]
            )
        )
    if "state" in data:
        import capo_amplifyuibuilder.types.mutation_action_set_state_parameter

        out["state"] = (
            capo_amplifyuibuilder.types.mutation_action_set_state_parameter.deserialize_json(
                data["state"]
            )
        )
    return out
