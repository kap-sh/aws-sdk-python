"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.e_tag_algorithm_family
    import aws_sdk_omics.types.fallback_location
    import aws_sdk_omics.types.sequence_store_arn
    import aws_sdk_omics.types.sequence_store_description
    import aws_sdk_omics.types.sequence_store_id
    import aws_sdk_omics.types.sequence_store_name
    import aws_sdk_omics.types.sequence_store_status
    import aws_sdk_omics.types.sequence_store_status_message
    import aws_sdk_omics.types.sse_config


class SequenceStoreDetail(TypedDict):
    arn: "aws_sdk_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The store's ARN.</p>"""
    id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""
    name: NotRequired["aws_sdk_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>The store's server-side encryption (SSE) settings.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""
    fallback_location: NotRequired[
        "aws_sdk_omics.types.fallback_location.FallbackLocation"
    ]
    """<p> An S3 location that is used to store files that have failed a direct upload. </p>"""
    e_tag_algorithm_family: NotRequired[
        "aws_sdk_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The algorithm family of the ETag.</p>"""
    status: NotRequired["aws_sdk_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>Status of the sequence store.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The last-updated time of the Sequence Store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreDetail) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import aws_sdk_omics.types.sse_config

        out["sseConfig"] = aws_sdk_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "update_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["updateTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["update_time"]
        )
    return out


def deserialize_json(data: dict) -> SequenceStoreDetail:
    out: SequenceStoreDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SequenceStoreDetail.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SequenceStoreDetail.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sseConfig" in data:
        import aws_sdk_omics.types.sse_config

        out["sse_config"] = aws_sdk_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("SequenceStoreDetail.creation_time required")
    if "fallbackLocation" in data:
        out["fallback_location"] = data["fallbackLocation"]
    if "eTagAlgorithmFamily" in data:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "updateTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["update_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    return out
