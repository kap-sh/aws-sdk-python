"""Generated from Smithy shape ``com.amazonaws.macie2#GetSensitivityInspectionTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.sensitivity_inspection_template_excludes
    import capo_macie2.types.sensitivity_inspection_template_id
    import capo_macie2.types.sensitivity_inspection_template_includes


class GetSensitivityInspectionTemplateResponse(TypedDict, closed=True):
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The custom description of the template.</p>"""
    excludes: NotRequired[
        "capo_macie2.types.sensitivity_inspection_template_excludes.SensitivityInspectionTemplateExcludes"
    ]
    """<p>The managed data identifiers that are explicitly excluded (not used) when performing automated sensitive data discovery.</p>"""
    includes: NotRequired[
        "capo_macie2.types.sensitivity_inspection_template_includes.SensitivityInspectionTemplateIncludes"
    ]
    """<p>The allow lists, custom data identifiers, and managed data identifiers that are explicitly included (used) when performing automated sensitive data discovery.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the template: automated-sensitive-data-discovery.</p>"""
    sensitivity_inspection_template_id: NotRequired[
        "capo_macie2.types.sensitivity_inspection_template_id.SensitivityInspectionTemplateId"
    ]
    """<p>The unique identifier for the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSensitivityInspectionTemplateResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "excludes" in value:
        import capo_macie2.types.sensitivity_inspection_template_excludes

        out["excludes"] = (
            capo_macie2.types.sensitivity_inspection_template_excludes.serialize_json(
                value["excludes"]
            )
        )
    if "includes" in value:
        import capo_macie2.types.sensitivity_inspection_template_includes

        out["includes"] = (
            capo_macie2.types.sensitivity_inspection_template_includes.serialize_json(
                value["includes"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "sensitivity_inspection_template_id" in value:
        out["sensitivityInspectionTemplateId"] = value[
            "sensitivity_inspection_template_id"
        ]
    return out


def deserialize_json(data: dict) -> GetSensitivityInspectionTemplateResponse:
    out: GetSensitivityInspectionTemplateResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "excludes" in data:
        import capo_macie2.types.sensitivity_inspection_template_excludes

        out["excludes"] = (
            capo_macie2.types.sensitivity_inspection_template_excludes.deserialize_json(
                data["excludes"]
            )
        )
    if "includes" in data:
        import capo_macie2.types.sensitivity_inspection_template_includes

        out["includes"] = (
            capo_macie2.types.sensitivity_inspection_template_includes.deserialize_json(
                data["includes"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "sensitivityInspectionTemplateId" in data:
        out["sensitivity_inspection_template_id"] = data[
            "sensitivityInspectionTemplateId"
        ]
    return out
