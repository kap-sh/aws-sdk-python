"""Generated from Smithy shape ``com.amazonaws.macie2#SensitivityInspectionTemplateExcludes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string


class SensitivityInspectionTemplateExcludes(TypedDict, closed=True):
    managed_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each managed data identifier to exclude. To retrieve a list of valid values, use the ListManagedDataIdentifiers operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitivityInspectionTemplateExcludes) -> dict:
    out: dict = {}
    if "managed_data_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["managedDataIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["managed_data_identifier_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SensitivityInspectionTemplateExcludes:
    out: SensitivityInspectionTemplateExcludes = {}  # type: ignore[typeddict-item]
    if "managedDataIdentifierIds" in data:
        import capo_macie2.types.__list_of__string

        out["managed_data_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["managedDataIdentifierIds"]
            )
        )
    return out
