"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_failure_list
    import aws_sdk_ecr.types.image_list


class BatchGetImageResponse(TypedDict, closed=True):
    images: NotRequired["aws_sdk_ecr.types.image_list.ImageList"]
    """<p>A list of image objects corresponding to the image references in the request.</p>"""
    failures: NotRequired["aws_sdk_ecr.types.image_failure_list.ImageFailureList"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetImageResponse) -> dict:
    out: dict = {}
    if "images" in value:
        import aws_sdk_ecr.types.image_list

        out["images"] = aws_sdk_ecr.types.image_list.serialize_aws_json_1_1(
            value["images"]
        )
    if "failures" in value:
        import aws_sdk_ecr.types.image_failure_list

        out["failures"] = aws_sdk_ecr.types.image_failure_list.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetImageResponse:
    out: BatchGetImageResponse = {}  # type: ignore[typeddict-item]
    if "images" in data:
        import aws_sdk_ecr.types.image_list

        out["images"] = aws_sdk_ecr.types.image_list.deserialize_aws_json_1_1(
            data["images"]
        )
    if "failures" in data:
        import aws_sdk_ecr.types.image_failure_list

        out["failures"] = aws_sdk_ecr.types.image_failure_list.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
