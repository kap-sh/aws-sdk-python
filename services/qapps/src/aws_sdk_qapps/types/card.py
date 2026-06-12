"""Generated from Smithy shape ``com.amazonaws.qapps#Card``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qapps.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.file_upload_card
    import aws_sdk_qapps.types.form_input_card
    import aws_sdk_qapps.types.q_plugin_card
    import aws_sdk_qapps.types.q_query_card
    import aws_sdk_qapps.types.text_input_card


class _Card_textInput(TypedDict):
    textInput: "aws_sdk_qapps.types.text_input_card.TextInputCard"


class _Card_qQuery(TypedDict):
    qQuery: "aws_sdk_qapps.types.q_query_card.QQueryCard"


class _Card_qPlugin(TypedDict):
    qPlugin: "aws_sdk_qapps.types.q_plugin_card.QPluginCard"


class _Card_fileUpload(TypedDict):
    fileUpload: "aws_sdk_qapps.types.file_upload_card.FileUploadCard"


class _Card_formInput(TypedDict):
    formInput: "aws_sdk_qapps.types.form_input_card.FormInputCard"


Card: TypeAlias = (
    _Card_textInput | _Card_qQuery | _Card_qPlugin | _Card_fileUpload | _Card_formInput
)


# --- restJson1 ser/de ---
def serialize_json(value: Card) -> dict:
    if "textInput" in value:
        import aws_sdk_qapps.types.text_input_card

        return {
            "textInput": aws_sdk_qapps.types.text_input_card.serialize_json(
                value["textInput"]
            )
        }
    elif "qQuery" in value:
        import aws_sdk_qapps.types.q_query_card

        return {
            "qQuery": aws_sdk_qapps.types.q_query_card.serialize_json(value["qQuery"])
        }
    elif "qPlugin" in value:
        import aws_sdk_qapps.types.q_plugin_card

        return {
            "qPlugin": aws_sdk_qapps.types.q_plugin_card.serialize_json(
                value["qPlugin"]
            )
        }
    elif "fileUpload" in value:
        import aws_sdk_qapps.types.file_upload_card

        return {
            "fileUpload": aws_sdk_qapps.types.file_upload_card.serialize_json(
                value["fileUpload"]
            )
        }
    elif "formInput" in value:
        import aws_sdk_qapps.types.form_input_card

        return {
            "formInput": aws_sdk_qapps.types.form_input_card.serialize_json(
                value["formInput"]
            )
        }
    else:
        raise SerializationError("Card: no variant present")


def deserialize_json(data: dict) -> Card:
    if "textInput" in data:
        import aws_sdk_qapps.types.text_input_card

        return {
            "textInput": aws_sdk_qapps.types.text_input_card.deserialize_json(
                data["textInput"]
            )
        }
    elif "qQuery" in data:
        import aws_sdk_qapps.types.q_query_card

        return {
            "qQuery": aws_sdk_qapps.types.q_query_card.deserialize_json(data["qQuery"])
        }
    elif "qPlugin" in data:
        import aws_sdk_qapps.types.q_plugin_card

        return {
            "qPlugin": aws_sdk_qapps.types.q_plugin_card.deserialize_json(
                data["qPlugin"]
            )
        }
    elif "fileUpload" in data:
        import aws_sdk_qapps.types.file_upload_card

        return {
            "fileUpload": aws_sdk_qapps.types.file_upload_card.deserialize_json(
                data["fileUpload"]
            )
        }
    elif "formInput" in data:
        import aws_sdk_qapps.types.form_input_card

        return {
            "formInput": aws_sdk_qapps.types.form_input_card.deserialize_json(
                data["formInput"]
            )
        }
    else:
        raise DeserializationError("Card: no recognized variant key")
