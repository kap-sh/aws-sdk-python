"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.batch_result_error_entry_list
    import aws_sdk_sns.types.publish_batch_result_entry_list


class PublishBatchResponse(TypedDict):
    successful: NotRequired[
        "aws_sdk_sns.types.publish_batch_result_entry_list.PublishBatchResultEntryList"
    ]
    """<p>A list of successful <code>PublishBatch</code> responses.</p>"""
    failed: NotRequired[
        "aws_sdk_sns.types.batch_result_error_entry_list.BatchResultErrorEntryList"
    ]
    """<p>A list of failed <code>PublishBatch</code> responses. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful" in value:
        import aws_sdk_sns.types.publish_batch_result_entry_list

        aws_sdk_sns.types.publish_batch_result_entry_list.serialize_query(
            value["successful"], pairs, f"{prefix}.Successful"
        )
    if "failed" in value:
        import aws_sdk_sns.types.batch_result_error_entry_list

        aws_sdk_sns.types.batch_result_error_entry_list.serialize_query(
            value["failed"], pairs, f"{prefix}.Failed"
        )


def deserialize_query(el: Element) -> PublishBatchResponse:
    out: PublishBatchResponse = {}  # type: ignore[typeddict-item]
    child_successful = el.find("Successful")
    if child_successful is not None:
        import aws_sdk_sns.types.publish_batch_result_entry_list

        out["successful"] = (
            aws_sdk_sns.types.publish_batch_result_entry_list.deserialize_query(
                child_successful
            )
        )
    child_failed = el.find("Failed")
    if child_failed is not None:
        import aws_sdk_sns.types.batch_result_error_entry_list

        out["failed"] = (
            aws_sdk_sns.types.batch_result_error_entry_list.deserialize_query(
                child_failed
            )
        )
    return out
