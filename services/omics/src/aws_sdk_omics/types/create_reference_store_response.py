"""Generated from Smithy shape ``com.amazonaws.omics#CreateReferenceStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.reference_store_arn
    import aws_sdk_omics.types.reference_store_description
    import aws_sdk_omics.types.reference_store_id
    import aws_sdk_omics.types.reference_store_name
    import aws_sdk_omics.types.sse_config


class CreateReferenceStoreResponse(TypedDict, closed=True):
    id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The store's ID.</p>"""
    arn: "aws_sdk_omics.types.reference_store_arn.ReferenceStoreArn"
    """<p>The store's ARN.</p>"""
    name: NotRequired["aws_sdk_omics.types.reference_store_name.ReferenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.reference_store_description.ReferenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["aws_sdk_omics.types.sse_config.SseConfig"]
    """<p>The store's SSE settings.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReferenceStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
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
    return out


def deserialize_json(data: dict) -> CreateReferenceStoreResponse:
    out: CreateReferenceStoreResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateReferenceStoreResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateReferenceStoreResponse.arn required")
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
        raise DeserializationError(
            "CreateReferenceStoreResponse.creation_time required"
        )
    return out
