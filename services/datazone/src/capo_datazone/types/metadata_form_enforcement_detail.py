"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormEnforcementDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.required_metadata_form_list


class MetadataFormEnforcementDetail(TypedDict, closed=True):
    required_metadata_forms: NotRequired[
        "capo_datazone.types.required_metadata_form_list.RequiredMetadataFormList"
    ]
    """<p>The required metadata forms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormEnforcementDetail) -> dict:
    out: dict = {}
    if "required_metadata_forms" in value:
        import capo_datazone.types.required_metadata_form_list

        out["requiredMetadataForms"] = (
            capo_datazone.types.required_metadata_form_list.serialize_json(
                value["required_metadata_forms"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataFormEnforcementDetail:
    out: MetadataFormEnforcementDetail = {}  # type: ignore[typeddict-item]
    if "requiredMetadataForms" in data:
        import capo_datazone.types.required_metadata_form_list

        out["required_metadata_forms"] = (
            capo_datazone.types.required_metadata_form_list.deserialize_json(
                data["requiredMetadataForms"]
            )
        )
    return out
