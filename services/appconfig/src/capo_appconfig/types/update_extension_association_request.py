"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateExtensionAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id
    import capo_appconfig.types.parameter_value_map


class UpdateExtensionAssociationRequest(TypedDict, closed=True):
    extension_association_id: "capo_appconfig.types.id.Id"
    """<p>The system-generated ID for the association.</p>"""
    parameters: NotRequired[
        "capo_appconfig.types.parameter_value_map.ParameterValueMap"
    ]
    """<p>The parameter names and values defined in the extension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExtensionAssociationRequest) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_appconfig.types.parameter_value_map

        out["Parameters"] = capo_appconfig.types.parameter_value_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> UpdateExtensionAssociationRequest:
    out: UpdateExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Parameters" in data:
        import capo_appconfig.types.parameter_value_map

        out["parameters"] = capo_appconfig.types.parameter_value_map.deserialize_json(
            data["Parameters"]
        )
    return out
