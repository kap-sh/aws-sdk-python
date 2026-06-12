"""Generated from Smithy shape ``com.amazonaws.qapps#CardInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qapps.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.file_upload_card_input
    import aws_sdk_qapps.types.form_input_card_input
    import aws_sdk_qapps.types.q_plugin_card_input
    import aws_sdk_qapps.types.q_query_card_input
    import aws_sdk_qapps.types.text_input_card_input


class _CardInput_textInput(TypedDict):
    textInput: "aws_sdk_qapps.types.text_input_card_input.TextInputCardInput"


class _CardInput_qQuery(TypedDict):
    qQuery: "aws_sdk_qapps.types.q_query_card_input.QQueryCardInput"


class _CardInput_qPlugin(TypedDict):
    qPlugin: "aws_sdk_qapps.types.q_plugin_card_input.QPluginCardInput"


class _CardInput_fileUpload(TypedDict):
    fileUpload: "aws_sdk_qapps.types.file_upload_card_input.FileUploadCardInput"


class _CardInput_formInput(TypedDict):
    formInput: "aws_sdk_qapps.types.form_input_card_input.FormInputCardInput"


CardInput: TypeAlias = (
    _CardInput_textInput
    | _CardInput_qQuery
    | _CardInput_qPlugin
    | _CardInput_fileUpload
    | _CardInput_formInput
)


# --- restJson1 ser/de ---
def serialize_json(value: CardInput) -> dict:
    if "textInput" in value:
        import aws_sdk_qapps.types.text_input_card_input

        return {
            "textInput": aws_sdk_qapps.types.text_input_card_input.serialize_json(
                value["textInput"]
            )
        }
    elif "qQuery" in value:
        import aws_sdk_qapps.types.q_query_card_input

        return {
            "qQuery": aws_sdk_qapps.types.q_query_card_input.serialize_json(
                value["qQuery"]
            )
        }
    elif "qPlugin" in value:
        import aws_sdk_qapps.types.q_plugin_card_input

        return {
            "qPlugin": aws_sdk_qapps.types.q_plugin_card_input.serialize_json(
                value["qPlugin"]
            )
        }
    elif "fileUpload" in value:
        import aws_sdk_qapps.types.file_upload_card_input

        return {
            "fileUpload": aws_sdk_qapps.types.file_upload_card_input.serialize_json(
                value["fileUpload"]
            )
        }
    elif "formInput" in value:
        import aws_sdk_qapps.types.form_input_card_input

        return {
            "formInput": aws_sdk_qapps.types.form_input_card_input.serialize_json(
                value["formInput"]
            )
        }
    else:
        raise SerializationError("CardInput: no variant present")


def deserialize_json(data: dict) -> CardInput:
    if "textInput" in data:
        import aws_sdk_qapps.types.text_input_card_input

        return {
            "textInput": aws_sdk_qapps.types.text_input_card_input.deserialize_json(
                data["textInput"]
            )
        }
    elif "qQuery" in data:
        import aws_sdk_qapps.types.q_query_card_input

        return {
            "qQuery": aws_sdk_qapps.types.q_query_card_input.deserialize_json(
                data["qQuery"]
            )
        }
    elif "qPlugin" in data:
        import aws_sdk_qapps.types.q_plugin_card_input

        return {
            "qPlugin": aws_sdk_qapps.types.q_plugin_card_input.deserialize_json(
                data["qPlugin"]
            )
        }
    elif "fileUpload" in data:
        import aws_sdk_qapps.types.file_upload_card_input

        return {
            "fileUpload": aws_sdk_qapps.types.file_upload_card_input.deserialize_json(
                data["fileUpload"]
            )
        }
    elif "formInput" in data:
        import aws_sdk_qapps.types.form_input_card_input

        return {
            "formInput": aws_sdk_qapps.types.form_input_card_input.deserialize_json(
                data["formInput"]
            )
        }
    else:
        raise DeserializationError("CardInput: no recognized variant key")
