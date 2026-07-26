"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.batch_result_error_entry_list
    import capo_sns.types.publish_batch_result_entry_list


class PublishBatchResponse(TypedDict, closed=True):
    successful: NotRequired[
        "capo_sns.types.publish_batch_result_entry_list.PublishBatchResultEntryList"
    ]
    """<p>A list of successful <code>PublishBatch</code> responses.</p>"""
    failed: NotRequired[
        "capo_sns.types.batch_result_error_entry_list.BatchResultErrorEntryList"
    ]
    """<p>A list of failed <code>PublishBatch</code> responses. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful" in value:
        import capo_sns.types.publish_batch_result_entry_list

        capo_sns.types.publish_batch_result_entry_list.serialize_query(
            value["successful"], pairs, f"{prefix}.Successful"
        )
    if "failed" in value:
        import capo_sns.types.batch_result_error_entry_list

        capo_sns.types.batch_result_error_entry_list.serialize_query(
            value["failed"], pairs, f"{prefix}.Failed"
        )


def deserialize_query(el: Element) -> PublishBatchResponse:
    out: PublishBatchResponse = {}  # type: ignore[typeddict-item]
    child_successful = el.find("Successful")
    if child_successful is not None:
        import capo_sns.types.publish_batch_result_entry_list

        out["successful"] = (
            capo_sns.types.publish_batch_result_entry_list.deserialize_query(
                child_successful
            )
        )
    child_failed = el.find("Failed")
    if child_failed is not None:
        import capo_sns.types.batch_result_error_entry_list

        out["failed"] = capo_sns.types.batch_result_error_entry_list.deserialize_query(
            child_failed
        )
    return out
