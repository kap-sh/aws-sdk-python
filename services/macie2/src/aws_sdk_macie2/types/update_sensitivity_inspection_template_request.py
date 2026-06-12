"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateSensitivityInspectionTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.sensitivity_inspection_template_excludes
    import aws_sdk_macie2.types.sensitivity_inspection_template_includes


class UpdateSensitivityInspectionTemplateRequest(TypedDict):
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A custom description of the template. The description can contain as many as 200 characters.</p>"""
    excludes: NotRequired[
        "aws_sdk_macie2.types.sensitivity_inspection_template_excludes.SensitivityInspectionTemplateExcludes"
    ]
    """<p>The managed data identifiers to explicitly exclude (not use) when performing automated sensitive data discovery.</p> <p>To exclude an allow list or custom data identifier that's currently included by the template, update the values for the SensitivityInspectionTemplateIncludes.allowListIds and SensitivityInspectionTemplateIncludes.customDataIdentifierIds properties, respectively.</p>"""
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""
    includes: NotRequired[
        "aws_sdk_macie2.types.sensitivity_inspection_template_includes.SensitivityInspectionTemplateIncludes"
    ]
    """<p>The allow lists, custom data identifiers, and managed data identifiers to explicitly include (use) when performing automated sensitive data discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSensitivityInspectionTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "excludes" in value:
        import aws_sdk_macie2.types.sensitivity_inspection_template_excludes

        out["excludes"] = (
            aws_sdk_macie2.types.sensitivity_inspection_template_excludes.serialize_json(
                value["excludes"]
            )
        )
    if "includes" in value:
        import aws_sdk_macie2.types.sensitivity_inspection_template_includes

        out["includes"] = (
            aws_sdk_macie2.types.sensitivity_inspection_template_includes.serialize_json(
                value["includes"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSensitivityInspectionTemplateRequest:
    out: UpdateSensitivityInspectionTemplateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "excludes" in data:
        import aws_sdk_macie2.types.sensitivity_inspection_template_excludes

        out["excludes"] = (
            aws_sdk_macie2.types.sensitivity_inspection_template_excludes.deserialize_json(
                data["excludes"]
            )
        )
    if "includes" in data:
        import aws_sdk_macie2.types.sensitivity_inspection_template_includes

        out["includes"] = (
            aws_sdk_macie2.types.sensitivity_inspection_template_includes.deserialize_json(
                data["includes"]
            )
        )
    return out
