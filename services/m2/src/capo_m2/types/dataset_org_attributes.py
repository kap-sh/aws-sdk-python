"""Generated from Smithy shape ``com.amazonaws.m2#DatasetOrgAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_m2.types.gdg_attributes
    import capo_m2.types.po_attributes
    import capo_m2.types.ps_attributes
    import capo_m2.types.vsam_attributes


class _DatasetOrgAttributes_vsam(TypedDict, closed=True):
    vsam: "capo_m2.types.vsam_attributes.VsamAttributes"


class _DatasetOrgAttributes_gdg(TypedDict, closed=True):
    gdg: "capo_m2.types.gdg_attributes.GdgAttributes"


class _DatasetOrgAttributes_po(TypedDict, closed=True):
    po: "capo_m2.types.po_attributes.PoAttributes"


class _DatasetOrgAttributes_ps(TypedDict, closed=True):
    ps: "capo_m2.types.ps_attributes.PsAttributes"


DatasetOrgAttributes: TypeAlias = (
    _DatasetOrgAttributes_vsam
    | _DatasetOrgAttributes_gdg
    | _DatasetOrgAttributes_po
    | _DatasetOrgAttributes_ps
)


# --- restJson1 ser/de ---
def serialize_json(value: DatasetOrgAttributes) -> dict:
    if "vsam" in value:
        import capo_m2.types.vsam_attributes

        return {"vsam": capo_m2.types.vsam_attributes.serialize_json(value["vsam"])}
    elif "gdg" in value:
        import capo_m2.types.gdg_attributes

        return {"gdg": capo_m2.types.gdg_attributes.serialize_json(value["gdg"])}
    elif "po" in value:
        import capo_m2.types.po_attributes

        return {"po": capo_m2.types.po_attributes.serialize_json(value["po"])}
    elif "ps" in value:
        import capo_m2.types.ps_attributes

        return {"ps": capo_m2.types.ps_attributes.serialize_json(value["ps"])}
    else:
        raise SerializationError("DatasetOrgAttributes: no variant present")


def deserialize_json(data: dict) -> DatasetOrgAttributes:
    if "vsam" in data:
        import capo_m2.types.vsam_attributes

        return {"vsam": capo_m2.types.vsam_attributes.deserialize_json(data["vsam"])}
    elif "gdg" in data:
        import capo_m2.types.gdg_attributes

        return {"gdg": capo_m2.types.gdg_attributes.deserialize_json(data["gdg"])}
    elif "po" in data:
        import capo_m2.types.po_attributes

        return {"po": capo_m2.types.po_attributes.deserialize_json(data["po"])}
    elif "ps" in data:
        import capo_m2.types.ps_attributes

        return {"ps": capo_m2.types.ps_attributes.deserialize_json(data["ps"])}
    else:
        raise DeserializationError("DatasetOrgAttributes: no recognized variant key")
