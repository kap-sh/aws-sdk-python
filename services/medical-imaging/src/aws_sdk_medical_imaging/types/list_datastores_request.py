"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListDatastoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_status
    import aws_sdk_medical_imaging.types.next_token


class ListDatastoresRequest(TypedDict, closed=True):
    datastore_status: NotRequired[
        "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
    ]
    """<p>The data store status.</p>"""
    next_token: NotRequired["aws_sdk_medical_imaging.types.next_token.NextToken"]
    """<p>The pagination token used to request the list of data stores on the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>Valid Range: Minimum value of 1. Maximum value of 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatastoresRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatastoresRequest:
    out: ListDatastoresRequest = {}  # type: ignore[typeddict-item]
    return out
