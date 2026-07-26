"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetBulkPublishDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.bulk_publish_status
    import capo_cognito_sync.types.date
    import capo_cognito_sync.types.identity_pool_id
    import capo_cognito_sync.types.string


class GetBulkPublishDetailsResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    ]
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    bulk_publish_start_time: NotRequired["capo_cognito_sync.types.date.Date"]
    """The date/time at which the last bulk publish was initiated."""
    bulk_publish_complete_time: NotRequired["capo_cognito_sync.types.date.Date"]
    """If BulkPublishStatus is SUCCEEDED, the time the last bulk publish operation completed."""
    bulk_publish_status: NotRequired[
        "capo_cognito_sync.types.bulk_publish_status.BulkPublishStatus"
    ]
    """Status of the last bulk publish operation, valid values are: <p>NOT_STARTED - No bulk publish has been requested for this identity pool</p> <p>IN_PROGRESS - Data is being published to the configured stream</p> <p>SUCCEEDED - All data for the identity pool has been published to the configured stream</p> <p>FAILED - Some portion of the data has failed to publish, check FailureMessage for the cause.</p>"""
    failure_message: NotRequired["capo_cognito_sync.types.string.String"]
    """If BulkPublishStatus is FAILED this field will contain the error message that caused the bulk publish to fail."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBulkPublishDetailsResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "bulk_publish_start_time" in value:
        import capo_cognito_sync.types.date

        out["BulkPublishStartTime"] = capo_cognito_sync.types.date.serialize_json(
            value["bulk_publish_start_time"]
        )
    if "bulk_publish_complete_time" in value:
        import capo_cognito_sync.types.date

        out["BulkPublishCompleteTime"] = capo_cognito_sync.types.date.serialize_json(
            value["bulk_publish_complete_time"]
        )
    if "bulk_publish_status" in value:
        import capo_cognito_sync.types.bulk_publish_status

        out["BulkPublishStatus"] = (
            capo_cognito_sync.types.bulk_publish_status.serialize_json(
                value["bulk_publish_status"]
            )
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> GetBulkPublishDetailsResponse:
    out: GetBulkPublishDetailsResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "BulkPublishStartTime" in data:
        import capo_cognito_sync.types.date

        out["bulk_publish_start_time"] = capo_cognito_sync.types.date.deserialize_json(
            data["BulkPublishStartTime"]
        )
    if "BulkPublishCompleteTime" in data:
        import capo_cognito_sync.types.date

        out["bulk_publish_complete_time"] = (
            capo_cognito_sync.types.date.deserialize_json(
                data["BulkPublishCompleteTime"]
            )
        )
    if "BulkPublishStatus" in data:
        import capo_cognito_sync.types.bulk_publish_status

        out["bulk_publish_status"] = (
            capo_cognito_sync.types.bulk_publish_status.deserialize_json(
                data["BulkPublishStatus"]
            )
        )
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    return out
