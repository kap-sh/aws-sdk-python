"""Generated from Smithy shape ``com.amazonaws.omics#GetS3AccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.s3_access_point_arn
    import aws_sdk_omics.types.s3_access_policy
    import aws_sdk_omics.types.store_id
    import aws_sdk_omics.types.store_type


class GetS3AccessPolicyResponse(TypedDict, closed=True):
    s3_access_point_arn: NotRequired[
        "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>The S3 access point ARN that has the access policy.</p>"""
    store_id: NotRequired["aws_sdk_omics.types.store_id.StoreId"]
    """<p>The Amazon Web Services-generated Sequence Store or Reference Store ID.</p>"""
    store_type: NotRequired["aws_sdk_omics.types.store_type.StoreType"]
    """<p>The type of store associated with the access point.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The time when the policy was last updated.</p>"""
    s3_access_policy: "aws_sdk_omics.types.s3_access_policy.S3AccessPolicy"
    """<p>The current resource policy that controls S3 access on the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetS3AccessPolicyResponse) -> dict:
    out: dict = {}
    if "s3_access_point_arn" in value:
        out["s3AccessPointArn"] = value["s3_access_point_arn"]
    if "store_id" in value:
        out["storeId"] = value["store_id"]
    if "store_type" in value:
        import aws_sdk_omics.types.store_type

        out["storeType"] = aws_sdk_omics.types.store_type.serialize_json(
            value["store_type"]
        )
    if "update_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["updateTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["update_time"]
        )
    out["s3AccessPolicy"] = value["s3_access_policy"]
    return out


def deserialize_json(data: dict) -> GetS3AccessPolicyResponse:
    out: GetS3AccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "s3AccessPointArn" in data:
        out["s3_access_point_arn"] = data["s3AccessPointArn"]
    if "storeId" in data:
        out["store_id"] = data["storeId"]
    if "storeType" in data:
        import aws_sdk_omics.types.store_type

        out["store_type"] = aws_sdk_omics.types.store_type.deserialize_json(
            data["storeType"]
        )
    if "updateTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["update_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    if "s3AccessPolicy" in data:
        out["s3_access_policy"] = data["s3AccessPolicy"]
    else:
        raise DeserializationError(
            "GetS3AccessPolicyResponse.s3_access_policy required"
        )
    return out
