"""Generated from Smithy shape ``com.amazonaws.ses#SendBulkTemplatedEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.bulk_email_destination_status_list


class SendBulkTemplatedEmailResponse(TypedDict, closed=True):
    status: "aws_sdk_ses.types.bulk_email_destination_status_list.BulkEmailDestinationStatusList"
    """<p>One object per intended recipient. Check each response object and retry any messages with a failure status. (Note that order of responses will be respective to order of destinations in the request.)Receipt rules enable you to specify which actions </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendBulkTemplatedEmailResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.bulk_email_destination_status_list

    aws_sdk_ses.types.bulk_email_destination_status_list.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> SendBulkTemplatedEmailResponse:
    out: SendBulkTemplatedEmailResponse = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ses.types.bulk_email_destination_status_list

        out["status"] = (
            aws_sdk_ses.types.bulk_email_destination_status_list.deserialize_query(
                child_status
            )
        )
    else:
        raise DeserializationError("SendBulkTemplatedEmailResponse.status required")
    return out
