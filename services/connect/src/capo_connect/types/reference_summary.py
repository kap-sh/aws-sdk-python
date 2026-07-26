"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.attachment_reference
    import capo_connect.types.date_reference
    import capo_connect.types.email_message_reference
    import capo_connect.types.email_reference
    import capo_connect.types.number_reference
    import capo_connect.types.string_reference
    import capo_connect.types.url_reference


class _ReferenceSummary_Url(TypedDict, closed=True):
    Url: "capo_connect.types.url_reference.UrlReference"


class _ReferenceSummary_Attachment(TypedDict, closed=True):
    Attachment: "capo_connect.types.attachment_reference.AttachmentReference"


class _ReferenceSummary_EmailMessage(TypedDict, closed=True):
    EmailMessage: "capo_connect.types.email_message_reference.EmailMessageReference"


class _ReferenceSummary_EmailMessageRedacted(TypedDict, closed=True):
    EmailMessageRedacted: (
        "capo_connect.types.email_message_reference.EmailMessageReference"
    )


class _ReferenceSummary_EmailMessagePlainText(TypedDict, closed=True):
    EmailMessagePlainText: (
        "capo_connect.types.email_message_reference.EmailMessageReference"
    )


class _ReferenceSummary_EmailMessagePlainTextRedacted(TypedDict, closed=True):
    EmailMessagePlainTextRedacted: (
        "capo_connect.types.email_message_reference.EmailMessageReference"
    )


class _ReferenceSummary_String(TypedDict, closed=True):
    String: "capo_connect.types.string_reference.StringReference"


class _ReferenceSummary_Number(TypedDict, closed=True):
    Number: "capo_connect.types.number_reference.NumberReference"


class _ReferenceSummary_Date(TypedDict, closed=True):
    Date: "capo_connect.types.date_reference.DateReference"


class _ReferenceSummary_Email(TypedDict, closed=True):
    Email: "capo_connect.types.email_reference.EmailReference"


ReferenceSummary: TypeAlias = (
    _ReferenceSummary_Url
    | _ReferenceSummary_Attachment
    | _ReferenceSummary_EmailMessage
    | _ReferenceSummary_EmailMessageRedacted
    | _ReferenceSummary_EmailMessagePlainText
    | _ReferenceSummary_EmailMessagePlainTextRedacted
    | _ReferenceSummary_String
    | _ReferenceSummary_Number
    | _ReferenceSummary_Date
    | _ReferenceSummary_Email
)


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceSummary) -> dict:
    if "Url" in value:
        import capo_connect.types.url_reference

        return {"Url": capo_connect.types.url_reference.serialize_json(value["Url"])}
    elif "Attachment" in value:
        import capo_connect.types.attachment_reference

        return {
            "Attachment": capo_connect.types.attachment_reference.serialize_json(
                value["Attachment"]
            )
        }
    elif "EmailMessage" in value:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessage": capo_connect.types.email_message_reference.serialize_json(
                value["EmailMessage"]
            )
        }
    elif "EmailMessageRedacted" in value:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessageRedacted": capo_connect.types.email_message_reference.serialize_json(
                value["EmailMessageRedacted"]
            )
        }
    elif "EmailMessagePlainText" in value:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessagePlainText": capo_connect.types.email_message_reference.serialize_json(
                value["EmailMessagePlainText"]
            )
        }
    elif "EmailMessagePlainTextRedacted" in value:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessagePlainTextRedacted": capo_connect.types.email_message_reference.serialize_json(
                value["EmailMessagePlainTextRedacted"]
            )
        }
    elif "String" in value:
        import capo_connect.types.string_reference

        return {
            "String": capo_connect.types.string_reference.serialize_json(
                value["String"]
            )
        }
    elif "Number" in value:
        import capo_connect.types.number_reference

        return {
            "Number": capo_connect.types.number_reference.serialize_json(
                value["Number"]
            )
        }
    elif "Date" in value:
        import capo_connect.types.date_reference

        return {"Date": capo_connect.types.date_reference.serialize_json(value["Date"])}
    elif "Email" in value:
        import capo_connect.types.email_reference

        return {
            "Email": capo_connect.types.email_reference.serialize_json(value["Email"])
        }
    else:
        raise SerializationError("ReferenceSummary: no variant present")


def deserialize_json(data: dict) -> ReferenceSummary:
    if "Url" in data:
        import capo_connect.types.url_reference

        return {"Url": capo_connect.types.url_reference.deserialize_json(data["Url"])}
    elif "Attachment" in data:
        import capo_connect.types.attachment_reference

        return {
            "Attachment": capo_connect.types.attachment_reference.deserialize_json(
                data["Attachment"]
            )
        }
    elif "EmailMessage" in data:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessage": capo_connect.types.email_message_reference.deserialize_json(
                data["EmailMessage"]
            )
        }
    elif "EmailMessageRedacted" in data:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessageRedacted": capo_connect.types.email_message_reference.deserialize_json(
                data["EmailMessageRedacted"]
            )
        }
    elif "EmailMessagePlainText" in data:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessagePlainText": capo_connect.types.email_message_reference.deserialize_json(
                data["EmailMessagePlainText"]
            )
        }
    elif "EmailMessagePlainTextRedacted" in data:
        import capo_connect.types.email_message_reference

        return {
            "EmailMessagePlainTextRedacted": capo_connect.types.email_message_reference.deserialize_json(
                data["EmailMessagePlainTextRedacted"]
            )
        }
    elif "String" in data:
        import capo_connect.types.string_reference

        return {
            "String": capo_connect.types.string_reference.deserialize_json(
                data["String"]
            )
        }
    elif "Number" in data:
        import capo_connect.types.number_reference

        return {
            "Number": capo_connect.types.number_reference.deserialize_json(
                data["Number"]
            )
        }
    elif "Date" in data:
        import capo_connect.types.date_reference

        return {
            "Date": capo_connect.types.date_reference.deserialize_json(data["Date"])
        }
    elif "Email" in data:
        import capo_connect.types.email_reference

        return {
            "Email": capo_connect.types.email_reference.deserialize_json(data["Email"])
        }
    else:
        raise DeserializationError("ReferenceSummary: no recognized variant key")
