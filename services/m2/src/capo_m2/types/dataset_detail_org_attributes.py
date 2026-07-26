"""Generated from Smithy shape ``com.amazonaws.m2#DatasetDetailOrgAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_m2.types.gdg_detail_attributes
    import capo_m2.types.po_detail_attributes
    import capo_m2.types.ps_detail_attributes
    import capo_m2.types.vsam_detail_attributes


class _DatasetDetailOrgAttributes_vsam(TypedDict, closed=True):
    vsam: "capo_m2.types.vsam_detail_attributes.VsamDetailAttributes"


class _DatasetDetailOrgAttributes_gdg(TypedDict, closed=True):
    gdg: "capo_m2.types.gdg_detail_attributes.GdgDetailAttributes"


class _DatasetDetailOrgAttributes_po(TypedDict, closed=True):
    po: "capo_m2.types.po_detail_attributes.PoDetailAttributes"


class _DatasetDetailOrgAttributes_ps(TypedDict, closed=True):
    ps: "capo_m2.types.ps_detail_attributes.PsDetailAttributes"


DatasetDetailOrgAttributes: TypeAlias = (
    _DatasetDetailOrgAttributes_vsam
    | _DatasetDetailOrgAttributes_gdg
    | _DatasetDetailOrgAttributes_po
    | _DatasetDetailOrgAttributes_ps
)


# --- restJson1 ser/de ---
def serialize_json(value: DatasetDetailOrgAttributes) -> dict:
    if "vsam" in value:
        import capo_m2.types.vsam_detail_attributes

        return {
            "vsam": capo_m2.types.vsam_detail_attributes.serialize_json(value["vsam"])
        }
    elif "gdg" in value:
        import capo_m2.types.gdg_detail_attributes

        return {"gdg": capo_m2.types.gdg_detail_attributes.serialize_json(value["gdg"])}
    elif "po" in value:
        import capo_m2.types.po_detail_attributes

        return {"po": capo_m2.types.po_detail_attributes.serialize_json(value["po"])}
    elif "ps" in value:
        import capo_m2.types.ps_detail_attributes

        return {"ps": capo_m2.types.ps_detail_attributes.serialize_json(value["ps"])}
    else:
        raise SerializationError("DatasetDetailOrgAttributes: no variant present")


def deserialize_json(data: dict) -> DatasetDetailOrgAttributes:
    if "vsam" in data:
        import capo_m2.types.vsam_detail_attributes

        return {
            "vsam": capo_m2.types.vsam_detail_attributes.deserialize_json(data["vsam"])
        }
    elif "gdg" in data:
        import capo_m2.types.gdg_detail_attributes

        return {
            "gdg": capo_m2.types.gdg_detail_attributes.deserialize_json(data["gdg"])
        }
    elif "po" in data:
        import capo_m2.types.po_detail_attributes

        return {"po": capo_m2.types.po_detail_attributes.deserialize_json(data["po"])}
    elif "ps" in data:
        import capo_m2.types.ps_detail_attributes

        return {"ps": capo_m2.types.ps_detail_attributes.deserialize_json(data["ps"])}
    else:
        raise DeserializationError(
            "DatasetDetailOrgAttributes: no recognized variant key"
        )
