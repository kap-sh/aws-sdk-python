"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.type_name


class BatchPutProfileObjectRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    items: "aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list.BatchPutProfileObjectRequestItemList"
    """<p>A list of items to add to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    import aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list

    out["Items"] = (
        aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectRequest:
    out: BatchPutProfileObjectRequest = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "BatchPutProfileObjectRequest.object_type_name required"
        )
    if "Items" in data:
        import aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list

        out["items"] = (
            aws_sdk_customer_profiles.types.batch_put_profile_object_request_item_list.deserialize_json(
                data["Items"]
            )
        )
    else:
        raise DeserializationError("BatchPutProfileObjectRequest.items required")
    return out
