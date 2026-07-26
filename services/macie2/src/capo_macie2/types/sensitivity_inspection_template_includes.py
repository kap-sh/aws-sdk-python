"""Generated from Smithy shape ``com.amazonaws.macie2#SensitivityInspectionTemplateIncludes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string


class SensitivityInspectionTemplateIncludes(TypedDict, closed=True):
    allow_list_ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of unique identifiers, one for each allow list to include.</p>"""
    custom_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each custom data identifier to include.</p>"""
    managed_data_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of unique identifiers, one for each managed data identifier to include.</p> <p>Amazon Macie uses these managed data identifiers in addition to managed data identifiers that are subsequently released and recommended for automated sensitive data discovery. To retrieve a list of valid values for the managed data identifiers that are currently available, use the ListManagedDataIdentifiers operation.</p> <para/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitivityInspectionTemplateIncludes) -> dict:
    out: dict = {}
    if "allow_list_ids" in value:
        import capo_macie2.types.__list_of__string

        out["allowListIds"] = capo_macie2.types.__list_of__string.serialize_json(
            value["allow_list_ids"]
        )
    if "custom_data_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["customDataIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["custom_data_identifier_ids"]
            )
        )
    if "managed_data_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["managedDataIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["managed_data_identifier_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SensitivityInspectionTemplateIncludes:
    out: SensitivityInspectionTemplateIncludes = {}  # type: ignore[typeddict-item]
    if "allowListIds" in data:
        import capo_macie2.types.__list_of__string

        out["allow_list_ids"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["allowListIds"]
        )
    if "customDataIdentifierIds" in data:
        import capo_macie2.types.__list_of__string

        out["custom_data_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["customDataIdentifierIds"]
            )
        )
    if "managedDataIdentifierIds" in data:
        import capo_macie2.types.__list_of__string

        out["managed_data_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["managedDataIdentifierIds"]
            )
        )
    return out
