"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyMappingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.create_missing_property
    import capo_iotsitewise.types.match_by_property_name
    import capo_iotsitewise.types.property_mappings


class PropertyMappingConfiguration(TypedDict, closed=True):
    match_by_property_name: (
        "capo_iotsitewise.types.match_by_property_name.MatchByPropertyName"
    )
    """<p>If true, properties are matched by name between the interface asset model and the asset model where the interface is applied.</p>"""
    create_missing_property: (
        "capo_iotsitewise.types.create_missing_property.CreateMissingProperty"
    )
    """<p>If true, missing properties from the interface asset model are automatically created in the asset model where the interface is applied.</p>"""
    overrides: NotRequired["capo_iotsitewise.types.property_mappings.PropertyMappings"]
    """<p>A list of specific property mappings that override the automatic mapping by name when an interface is applied to an asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyMappingConfiguration) -> dict:
    out: dict = {}
    out["matchByPropertyName"] = value.get("match_by_property_name", False)
    out["createMissingProperty"] = value.get("create_missing_property", False)
    if "overrides" in value:
        import capo_iotsitewise.types.property_mappings

        out["overrides"] = capo_iotsitewise.types.property_mappings.serialize_json(
            value["overrides"]
        )
    return out


def deserialize_json(data: dict) -> PropertyMappingConfiguration:
    out: PropertyMappingConfiguration = {}  # type: ignore[typeddict-item]
    if "matchByPropertyName" in data:
        out["match_by_property_name"] = data["matchByPropertyName"]
    else:
        out["match_by_property_name"] = False
    if "createMissingProperty" in data:
        out["create_missing_property"] = data["createMissingProperty"]
    else:
        out["create_missing_property"] = False
    if "overrides" in data:
        import capo_iotsitewise.types.property_mappings

        out["overrides"] = capo_iotsitewise.types.property_mappings.deserialize_json(
            data["overrides"]
        )
    return out
