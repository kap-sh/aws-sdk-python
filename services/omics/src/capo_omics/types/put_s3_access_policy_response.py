"""Generated from Smithy shape ``com.amazonaws.omics#PutS3AccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.s3_access_point_arn
    import capo_omics.types.store_id
    import capo_omics.types.store_type


class PutS3AccessPolicyResponse(TypedDict, closed=True):
    s3_access_point_arn: NotRequired[
        "capo_omics.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>The S3 access point ARN that now has the access policy.</p>"""
    store_id: NotRequired["capo_omics.types.store_id.StoreId"]
    """<p>The Amazon Web Services-generated Sequence Store or Reference Store ID.</p>"""
    store_type: NotRequired["capo_omics.types.store_type.StoreType"]
    """<p>The type of store associated with the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutS3AccessPolicyResponse) -> dict:
    out: dict = {}
    if "s3_access_point_arn" in value:
        out["s3AccessPointArn"] = value["s3_access_point_arn"]
    if "store_id" in value:
        out["storeId"] = value["store_id"]
    if "store_type" in value:
        import capo_omics.types.store_type

        out["storeType"] = capo_omics.types.store_type.serialize_json(
            value["store_type"]
        )
    return out


def deserialize_json(data: dict) -> PutS3AccessPolicyResponse:
    out: PutS3AccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "s3AccessPointArn" in data:
        out["s3_access_point_arn"] = data["s3AccessPointArn"]
    if "storeId" in data:
        out["store_id"] = data["storeId"]
    if "storeType" in data:
        import capo_omics.types.store_type

        out["store_type"] = capo_omics.types.store_type.deserialize_json(
            data["storeType"]
        )
    return out
