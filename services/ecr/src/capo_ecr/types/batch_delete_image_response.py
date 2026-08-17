"""Generated from Smithy shape ``com.amazonaws.ecr#BatchDeleteImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_failure_list
    import capo_ecr.types.image_identifier_list


class BatchDeleteImageResponse(TypedDict, closed=True):
    image_ids: NotRequired["capo_ecr.types.image_identifier_list.ImageIdentifierList"]
    """<p>The image IDs of the deleted images.</p>"""
    failures: NotRequired["capo_ecr.types.image_failure_list.ImageFailureList"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImageResponse) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import capo_ecr.types.image_identifier_list

        out["imageIds"] = capo_ecr.types.image_identifier_list.serialize_aws_json_1_1(
            value["image_ids"]
        )
    if "failures" in value:
        import capo_ecr.types.image_failure_list

        out["failures"] = capo_ecr.types.image_failure_list.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImageResponse:
    out: BatchDeleteImageResponse = {}  # type: ignore[typeddict-item]
    if data.get("imageIds") is not None:
        import capo_ecr.types.image_identifier_list

        out["image_ids"] = (
            capo_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    if data.get("failures") is not None:
        import capo_ecr.types.image_failure_list

        out["failures"] = capo_ecr.types.image_failure_list.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
