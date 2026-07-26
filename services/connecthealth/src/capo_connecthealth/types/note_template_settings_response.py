"""Generated from Smithy shape ``com.amazonaws.connecthealth#NoteTemplateSettingsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.custom_template_response
    import capo_connecthealth.types.managed_template_response


class _NoteTemplateSettingsResponse_managedTemplate(TypedDict, closed=True):
    managedTemplate: (
        "capo_connecthealth.types.managed_template_response.ManagedTemplateResponse"
    )


class _NoteTemplateSettingsResponse_customTemplate(TypedDict, closed=True):
    customTemplate: (
        "capo_connecthealth.types.custom_template_response.CustomTemplateResponse"
    )


NoteTemplateSettingsResponse: TypeAlias = (
    _NoteTemplateSettingsResponse_managedTemplate
    | _NoteTemplateSettingsResponse_customTemplate
)


# --- restJson1 ser/de ---
def serialize_json(value: NoteTemplateSettingsResponse) -> dict:
    if "managedTemplate" in value:
        import capo_connecthealth.types.managed_template_response

        return {
            "managedTemplate": capo_connecthealth.types.managed_template_response.serialize_json(
                value["managedTemplate"]
            )
        }
    elif "customTemplate" in value:
        import capo_connecthealth.types.custom_template_response

        return {
            "customTemplate": capo_connecthealth.types.custom_template_response.serialize_json(
                value["customTemplate"]
            )
        }
    else:
        raise SerializationError("NoteTemplateSettingsResponse: no variant present")


def deserialize_json(data: dict) -> NoteTemplateSettingsResponse:
    if "managedTemplate" in data:
        import capo_connecthealth.types.managed_template_response

        return {
            "managedTemplate": capo_connecthealth.types.managed_template_response.deserialize_json(
                data["managedTemplate"]
            )
        }
    elif "customTemplate" in data:
        import capo_connecthealth.types.custom_template_response

        return {
            "customTemplate": capo_connecthealth.types.custom_template_response.deserialize_json(
                data["customTemplate"]
            )
        }
    else:
        raise DeserializationError(
            "NoteTemplateSettingsResponse: no recognized variant key"
        )
