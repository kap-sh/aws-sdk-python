"""Generated from Smithy shape ``com.amazonaws.connecthealth#NoteTemplateSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.custom_template
    import capo_connecthealth.types.managed_template


class _NoteTemplateSettings_managedTemplate(TypedDict, closed=True):
    managedTemplate: "capo_connecthealth.types.managed_template.ManagedTemplate"


class _NoteTemplateSettings_customTemplate(TypedDict, closed=True):
    customTemplate: "capo_connecthealth.types.custom_template.CustomTemplate"


NoteTemplateSettings: TypeAlias = (
    _NoteTemplateSettings_managedTemplate | _NoteTemplateSettings_customTemplate
)


# --- restJson1 ser/de ---
def serialize_json(value: NoteTemplateSettings) -> dict:
    if "managedTemplate" in value:
        import capo_connecthealth.types.managed_template

        return {
            "managedTemplate": capo_connecthealth.types.managed_template.serialize_json(
                value["managedTemplate"]
            )
        }
    elif "customTemplate" in value:
        import capo_connecthealth.types.custom_template

        return {
            "customTemplate": capo_connecthealth.types.custom_template.serialize_json(
                value["customTemplate"]
            )
        }
    else:
        raise SerializationError("NoteTemplateSettings: no variant present")


def deserialize_json(data: dict) -> NoteTemplateSettings:
    if "managedTemplate" in data:
        import capo_connecthealth.types.managed_template

        return {
            "managedTemplate": capo_connecthealth.types.managed_template.deserialize_json(
                data["managedTemplate"]
            )
        }
    elif "customTemplate" in data:
        import capo_connecthealth.types.custom_template

        return {
            "customTemplate": capo_connecthealth.types.custom_template.deserialize_json(
                data["customTemplate"]
            )
        }
    else:
        raise DeserializationError("NoteTemplateSettings: no recognized variant key")
