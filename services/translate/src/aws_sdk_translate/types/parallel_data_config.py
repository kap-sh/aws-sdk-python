"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.parallel_data_format
    import aws_sdk_translate.types.s3_uri


class ParallelDataConfig(TypedDict):
    s3_uri: NotRequired["aws_sdk_translate.types.s3_uri.S3Uri"]
    """<p>The URI of the Amazon S3 folder that contains the parallel data input file. The folder must be in the same Region as the API endpoint you are calling.</p>"""
    format: NotRequired[
        "aws_sdk_translate.types.parallel_data_format.ParallelDataFormat"
    ]
    """<p>The format of the parallel data input file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "format" in value:
        import aws_sdk_translate.types.parallel_data_format

        out["Format"] = (
            aws_sdk_translate.types.parallel_data_format.serialize_aws_json_1_1(
                value["format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelDataConfig:
    out: ParallelDataConfig = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "Format" in data:
        import aws_sdk_translate.types.parallel_data_format

        out["format"] = (
            aws_sdk_translate.types.parallel_data_format.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    return out
