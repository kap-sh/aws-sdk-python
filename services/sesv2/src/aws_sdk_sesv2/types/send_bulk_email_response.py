"""Generated from Smithy shape ``com.amazonaws.sesv2#SendBulkEmailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.bulk_email_entry_result_list


class SendBulkEmailResponse(TypedDict):
    bulk_email_entry_results: (
        "aws_sdk_sesv2.types.bulk_email_entry_result_list.BulkEmailEntryResultList"
    )
    """<p>One object per intended recipient. Check each response object and retry any messages with a failure status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendBulkEmailResponse) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.bulk_email_entry_result_list

    out["BulkEmailEntryResults"] = (
        aws_sdk_sesv2.types.bulk_email_entry_result_list.serialize_json(
            value["bulk_email_entry_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendBulkEmailResponse:
    out: SendBulkEmailResponse = {}  # type: ignore[typeddict-item]
    if "BulkEmailEntryResults" in data:
        import aws_sdk_sesv2.types.bulk_email_entry_result_list

        out["bulk_email_entry_results"] = (
            aws_sdk_sesv2.types.bulk_email_entry_result_list.deserialize_json(
                data["BulkEmailEntryResults"]
            )
        )
    else:
        raise DeserializationError(
            "SendBulkEmailResponse.bulk_email_entry_results required"
        )
    return out
