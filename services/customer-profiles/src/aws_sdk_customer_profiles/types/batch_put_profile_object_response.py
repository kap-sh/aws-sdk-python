"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_put_profile_object_error_list
    import aws_sdk_customer_profiles.types.batch_put_profile_object_response_list


class BatchPutProfileObjectResponse(TypedDict, closed=True):
    successful: NotRequired[
        "aws_sdk_customer_profiles.types.batch_put_profile_object_response_list.BatchPutProfileObjectResponseList"
    ]
    """<p>A list of items that were successfully added to the domain.</p>"""
    failed: NotRequired[
        "aws_sdk_customer_profiles.types.batch_put_profile_object_error_list.BatchPutProfileObjectErrorList"
    ]
    """<p>A list of items that failed to be added to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import aws_sdk_customer_profiles.types.batch_put_profile_object_response_list

        out["Successful"] = (
            aws_sdk_customer_profiles.types.batch_put_profile_object_response_list.serialize_json(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_customer_profiles.types.batch_put_profile_object_error_list

        out["Failed"] = (
            aws_sdk_customer_profiles.types.batch_put_profile_object_error_list.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectResponse:
    out: BatchPutProfileObjectResponse = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_customer_profiles.types.batch_put_profile_object_response_list

        out["successful"] = (
            aws_sdk_customer_profiles.types.batch_put_profile_object_response_list.deserialize_json(
                data["Successful"]
            )
        )
    if "Failed" in data:
        import aws_sdk_customer_profiles.types.batch_put_profile_object_error_list

        out["failed"] = (
            aws_sdk_customer_profiles.types.batch_put_profile_object_error_list.deserialize_json(
                data["Failed"]
            )
        )
    return out
